use anchor_lang::prelude::*;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod myepicproject {
  use super::*;
  pub fn start_stuff_off(ctx: Context<StartStuffOff>) -> ProgramResult {
    //get a mutable reference to base_account
    let base_account = &mut ctx.accounts.base_account; // without &mut, we'd simply be working w/ a "local copy" of base_account.
    // Initialize total_gifs.
    base_account.total_gifs = 0;
    Ok(())
  }

  pub fn add_gif(ctx: Context<AddGif>, gif_link: String) -> ProgramResult {

    // extract these vars from Context to local mutable references
    let base_account = &mut ctx.accounts.base_account;
    let user = &mut ctx.accounts.user;
    base_account.gif_list.push(
        ItemStruct {
            gif_link: gif_link.to_string(),
            user_address: *user.to_account_info().key,
        }
    );
    base_account.total_gifs += 1;
    Ok(())
  }
}

// Attach certain variables to the StartStuffOff context.
// how to initialize it and what to hold in our StartStuffOff context
#[derive(Accounts)]
pub struct StartStuffOff<'info> {
    // init-create a new account owned by this program.
    // payer is the user calling the function. "rent". Without rent, account will be cleared (eviction LOL)
    // allocate 9000 bytes of space
    #[account(init, payer = user, space = 9000)]
    pub base_account: Account<'info, BaseAccount>,
    #[account(mut)]
    pub user: Signer<'info>, // user data pssed into the program to prove that's they own the wallet account
    pub system_program: Program <'info, System>, // system_program is the main program that runs solana. it's created by solana creator and its id = 11111111111111111111111111111111
}

// Specify what data you want in the AddGif Context.
#[derive(Accounts)]
pub struct AddGif<'info> {
    // allow access to a mutable reference to base_account, so I can change the total_gifs value stored there
    #[account(mut)] // without this, fn only changes the var in the fn.
    pub base_account: Account<'info, BaseAccount>,
    #[account(mut)]
    pub user: Signer<'info>, // adding Signer so the fn can write to accounts
}

// Create a custom struct for us to work with.
#[derive(Debug, Clone, AnchorSerialize, AnchorDeserialize)] // serialize data into birnary format into accounts and de-serialize fr/
pub struct ItemStruct {
    pub gif_link: String,
    pub user_address: Pubkey,
}

// Tell Solana what we want to store on this account.
#[account]
pub struct BaseAccount { // create an account
    pub total_gifs: u64, // and store this var inside
    pub gif_list: Vec<ItemStruct>, // basically an array of ItemStruct which is custom struct
}