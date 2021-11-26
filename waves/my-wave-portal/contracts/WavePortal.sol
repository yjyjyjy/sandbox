// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

import "hardhat/console.sol";

contract WavePortal {

  uint256 totalWaves;
  mapping (address=>uint) waveCounter;

  constructor() {
      console.log("Yo yo, I am a contract and I am smart");
  }

  function wave() public {
    totalWaves += 1;
    waveCounter[msg.sender] += 1;
    console.log("%s has waved!", msg.sender);
    console.log("%s have %d wave(s)!", msg.sender, waveCounter[msg.sender]);
  }

  function getTotalWaves() public view returns (uint256) {
    console.log("We have %d total waves!", totalWaves);
    return totalWaves;
  }

}