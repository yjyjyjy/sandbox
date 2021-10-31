require("@nomiclabs/hardhat-waffle");
if (process.env.NODE_ENV !== 'production') {
  require('dotenv').config();
}
console.log(process.env.ALCHEMY_API_KEY);

// Go to https://www.alchemyapi.io, sign up, create
// a new App in its dashboard, and replace "KEY" with its key

// Replace this private key with your Ropsten account private key
// To export your private key from Metamask, open Metamask and
// go to Account Details > Export Private Key
// Be aware of NEVER putting real Ether into testing accounts

module.exports = {
  defaultNetwork:"kovan",
  solidity: "0.8.7",
  networks: {
    hardhat: {
    },
    kovan: {
      url: `https://eth-kovan.alchemyapi.io/v2/${process.env.ALCHEMY_API_KEY}`,
      accounts: [`0x${process.env.KOVAN_PRIVATE_KEY}`]
    }
  }
};
