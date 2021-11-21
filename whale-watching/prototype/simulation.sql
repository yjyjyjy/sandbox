/*
I want to get a list of whales and track what they are buying now. I want to catch the trend early on.
*/

-- 1. The top 100 nft wallets since Aug 2021
-- 2. The new collection of them at the week before

-- the week dates to be used
with dates_of_interest as (
  select
      first_day_of_week
      , dt
  from dune_user_generated.calendar
  where first_day_of_week > '2021-08-01'
)
, ownership_undeduped as (
  select
    d.first_day_of_week as week
    , "tokenId" as token_id
    , contract_address
    , "to" as owner_address_raw
    , evt_block_number
    , evt_block_time >= (d.first_day_of_week - interval '7 days') as past_7_day_purchase
  from erc721."ERC721_evt_Transfer" t
  join dates_of_interest d
    on t.evt_block_time < d.first_day_of_week
  where "to" not in (
        '\x0000000000000000000000000000000000000000' -- burned
        , '\xe052113bd7d7700d623414a0a4585bcae754e9d5'-- nifty-gateway-omnibus
        , '\x959e104e1a4db6317fa58f8295f586e1a978c297'-- decentraland
        )
    and contract_address not in (
        '\x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85' --ENS
        )
)
, last_ownership as (
  select
    week
    , token_id
    , contract_address
    , owner_address_raw
    , past_7_day_purchase
  from (
    select
      week
      , token_id
      , contract_address
      , owner_address_raw
      , past_7_day_purchase
      , row_number() over (partition by week, contract_address, token_id order by evt_block_number desc) as rnk
    from ownership_undeduped
  ) a
  where rnk = 1
)
select *
from last_ownership
limit 100;







with nft_last_ownership as ( -- NFT's current owner
    select
        token_id
        , contract_address
        , owner_address_raw
        , REPLACE (owner_address_raw::text, '\x', '0x') as owner_address
        , past_7_day_purchase


            select
            week
            , token_id
            , contract_address
            , owner_address_raw
            , evt_block_number
            ,
            , row_number() over (partition by date_trunc('week',evt_block_time), contract_address, "tokenId" order by evt_block_number desc) as rnk
    from (
        select
            date_trunc('week',evt_block_time) as week -- by week
            , "tokenId" as token_id
            , contract_address
            , "to" as owner_address_raw
            , evt_block_number
            , evt_block_time >= (now() - interval '7 days') as past_7_day_purchase

        from erc721."ERC721_evt_Transfer"
        where 1=1 -- contract_address = '\xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d' -- BAYC
            and evt_block_time <= NOW()
            and evt_block_time >= date '2021-11-01'
            and "to" not in (
                '\x0000000000000000000000000000000000000000' -- burned
                , '\xe052113bd7d7700d623414a0a4585bcae754e9d5'-- nifty-gateway-omnibus
                , '\x959e104e1a4db6317fa58f8295f586e1a978c297'-- decentraland
                )
            and contract_address not in (
                '\x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85' --Ethereum Name Service (ENS)
                )

    ) a
    where rnk = 1
)
, ownership_scrubbed as (
    select o.*
    from nft_last_ownership o
    join (
          select
              owner_address
          from nft_last_ownership
          group by 1
          having count(distinct token_id) < 99999 -- otherwise likely marketplace account
        ) m
        on o.owner_address = m.owner_address
    join (
          select
              owner_address
              , contract_address
          from nft_last_ownership
          group by 1,2
          having count(distinct token_id) < 500 -- otherwise likely the owner contract of a project with left over items
        ) l
        on o.owner_address = l.owner_address
        and o.contract_address = l.contract_address
)
, labels as (
    select
        address
        , labels.get(address, 'ens name') as name
    from labels."labels"
    where type = 'ens name'
        and address is not null
        and name is not null
    group by 1,2
)
, floor_price as (
    select
        "nft_contract_address" as contract_address
        , nft_project_name
        , percentile_cont(.100) within group (order by usd_amount) as floor_price_usd
        , sum(number_of_items) trade_volume
    FROM nft.trades
    where 1=1-- "nft_contract_address"= ('\xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d')
        and original_amount > 0.0
        and "trade_type" = 'Single Item Trade'
        and "tx_from" != '0x0000000000000000000000000000000000000000'
        and block_time > now() - interval '30 days'
        AND original_amount_raw > 0
        and usd_amount > 0
    group by 1,2
    having sum(number_of_items) >= 5
)
, owner_collection as (
  select
    owner_address
    , owner_address_raw
    , o.contract_address
    , count(distinct token_id) as num_token
    , sum(floor_price_usd) as collection_worth
  from ownership_scrubbed o
  join floor_price p
      on p.contract_address = o.contract_address
  group by 1,2,3
)
, multi_collection_holders as (
select
    owner_address
  from (
    select
      owner_address
      , contract_address
      , num_token
      , collection_worth
      , row_number() over (partition by owner_address order by collection_worth desc) as rnk
    from owner_collection
  ) tmp
  group by 1
  having sum(case when rnk = 1 then collection_worth end)/sum(collection_worth) < 0.9 -- avoid one trick pony
)
, top_collectors as (
  select
    o.owner_address
    , sum(collection_worth) as total_wallet_worth
  from owner_collection o
  join multi_collection_holders m
    on o.owner_address = m.owner_address
  left join labels l
      on o.owner_address_raw = l.address
  group by 1
  order by total_wallet_worth desc
  limit 100
)
, project_name_mapping as (
  select
    contract_address
    , nft_project_name
  from floor_price
  group by 1,2
)
select
    REPLACE(o.contract_address::text, '\x', '0x') as contract_address
    , nft_project_name
    , count(distinct case when o.past_7_day_purchase then o.owner_address end) as num_noteable_collectors_collected_past_7d
    , count(distinct case when o.past_7_day_purchase then token_id end) as num_token_transferred_past_7d
    , count(distinct case when not o.past_7_day_purchase then o.owner_address end) as num_noteable_collectors_collected_prior_to_7d_ago
    , count(distinct case when not o.past_7_day_purchase then token_id end) as num_token_transferred_prior_to_7d_ago
from top_collectors t
join nft_last_ownership o
  on t.owner_address = o.owner_address
join project_name_mapping m
  on m.contract_address = o.contract_address
group by 1,2
having count(distinct case when o.past_7_day_purchase then o.owner_address end) >= 3
order by 3 desc
;


-- 3. The floor price of such collection in the following 60 days. group by cohort
