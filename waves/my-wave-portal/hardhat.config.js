require("dotenv").config();
require('@nomiclabs/hardhat-waffle');

module.exports = {
  solidity: '0.8.0',
  networks: {
    rinkeby: {
      url: process.env.RINKEBY_END_POINT,
      accounts: [process.env.DEV_ACCOUNT_PRIVATE_KEY]
    },
  },
};