# Backlog

This is what my backlog look like right now top of my head: not fully prioritized or exhaustive. Many are non critical.
1. Smart contract tests of transfers, reveal, royalty collection edit on opensea
2. Let user know they're not on mainnet
3. refresh browser on metamask network change: https://docs.ethers.io/v5/single-page/#/v5/concepts/best-practices/
4. Link to opensea right after minting - or instructions to how to do it
5. Connect MetaMask and mint button to work on mobile
6. [x]Logic for generator to parse file names to take in keyword from the prefix
7. [x]Create rest of website / links and additional sections
8. ypadding/ymargin responsive on mobile on top and bottom of images 
9.  Notification of not enough eth in wallet to mint
10. put in video under hero

# Full loop test

1. Take in images folder
2. Run script to pull in folder and file names to generate temp config
3. Update config with weights and dependency condition
4. Generate images
5. Pin images (but don't do anything with them yet)
6. Update metadata with pinned images URI
7. Pin metadata
8. Pin Unrevealed placeholder image
9. Pin Unrevealed placeholder metadata with Unrevealed placeholder image URI
10. Deploy smart contract with unrevealed placeholder metadata URI
11. Edit Collection on Opensea with royalty.
12. Deploy updated website to point to the new smart contractAddress and contractAbi (in contracts folder).
13. User mint NFTs from website
14. User able to see the NFT on opensea (but unrevealed)
15. Set Smart Contract to reveal with pinned metadata URI, opensea should see the updated revealed image (opensea testnet may not do a refresh so this could be tricky to check)
16. Test transfer of nft from one account to another
17. Test withdrawal of balance in smart contract
18. Test selling and buying on opensea to see royalty.


# Backlog for this module
1. View on opensea - can be just link to collection because link to individual nfts minted is hard UI wise when user mints say 10 NFTs, how to display the link? 
https://testnets.opensea.io/assets/0x319860a99bb6fda3ddaea0676dac38a349f2e62d/1
option 1: Can give them link to first item out out of 10 with instructions to change the 1 to 2 to see the rest
option 2: Can provide all 10 links like 
"View On OpenSea
1, 2, 3, 4, 5, 6, 7, 8, 9, 10"

TODO - detect and link to install metamask

TODO Metamask mobile wallet tonnect to work

## How to Install Fonts Setup Fonts to work with Chakra
1. Pick a google fonts
2. Copy the <link> and put it in index.html
3. Update theme fonts and textStyles
```
<link href="https://fonts.googleapis.com/css2?family=Amatic+SC:wght@400;700&display=swap" rel="stylesheet">
```

TODO Opensea link spacing mobile
TODO google lighthouse
TODO not mainnet detection