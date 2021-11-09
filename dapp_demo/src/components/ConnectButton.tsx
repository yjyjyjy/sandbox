// ConnectButton.tsx
import { Button, Box, Text } from "@chakra-ui/react";
import { useEthers, useEtherBalance } from "@usedapp/core";
import { ethers } from "ethers";

export default function ConnectButton() {

  const { activateBrowserWallet, account } = useEthers();
  const etherBalance = useEtherBalance(account);
  console.log(account)


  const provider = new ethers.providers.Web3Provider(window.ethereum, "any");
  console.log(provider)
  const signer = provider.getSigner();
  console.log("*******")
  console.log(signer)
  console.log(signer.getAddress())
  // // Prompt user for account connections
  // await provider.send("eth_requestAccounts", []);
  // const signer = provider.getSigner();
  // console.log("Account:", await signer.getAddress());


  return account ? (
    <Box>
      <Text color="white" fontSize="md">
        {/* {etherBalance && etherBalance.toNumber() / 1E18} ETH */}
        ETH
      </Text>
    </Box>
  ) : (
    <Button>Connect to a wallet</Button>
  );
}