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

// Tell Solana what we want to store on this account.
#[account]
pub struct BaseAccount { // create an account
    pub total_gifs: u64, // and store this var inside
}