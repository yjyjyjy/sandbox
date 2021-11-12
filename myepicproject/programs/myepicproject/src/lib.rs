use anchor_lang::prelude::*; // like import

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program] // macro-- declare this is a program
pub mod myepicproject { // this is like class in other lang
  use super::*;
  pub fn start_stuff_off(ctx: Context<StartStuffOff>) -> ProgramResult {
    Ok(())
  }
}

#[derive(Accounts)]
pub struct StartStuffOff {}