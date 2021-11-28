require("dotenv").config();
require('hardhat-abi-exporter');
require('@nomiclabs/hardhat-waffle');

module.exports = {
  solidity: '0.8.0',
  networks: {
    rinkeby: {
      url: process.env.RINKEBY_END_POINT,
      accounts: [process.env.DEV_ACCOUNT_PRIVATE_KEY]
    },
  },
  abiExporter: {
    path: './data/abi',
    clear: true,
    flat: false,
    only: [],
    spacing: 2,
    pretty: true,
  }
};