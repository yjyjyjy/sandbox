// scripts/index.js
// https://docs.alchemy.com/alchemy/tutorials/hello-world-smart-contract/interacting-with-a-smart-contract
const API_KEY = process.env.ALCHEMY_API_KEY;
const PRIVATE_KEY = process.env.KOVAN_PRIVATE_KEY;
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS;

const { ethers } = require('hardhat');
const contract = require('../artifacts/contracts/PriceConsumerV3.sol/PriceConsumerV3.json')

// Provider
const alchemyProvider = new ethers.providers.AlchemyProvider(network="kovan", API_KEY);
console.log(alchemyProvider);
console.log('AAAAAAAAAAA')
// Signer
console.log('0x'+PRIVATE_KEY)
const signer = new ethers.Wallet('0x'+PRIVATE_KEY, alchemyProvider);
console.log(signer);
console.log('BBBBBB')
// Contract
const priceContract = new ethers.Contract(CONTRACT_ADDRESS, contract.abi, signer);
console.log(priceContract);
console.log('CCCCC')

async function main () {
  // Retrieve accounts from the local node
  const accounts = await ethers.provider.listAccounts();
  console.log(accounts);
  const price = await priceContract.getLatestPrice()/10**8;
  console.log(price.toString());
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });


// 	0x115aff7117901174348822Ddb1ea989B258487ad