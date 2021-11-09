import { ethers } from "ethers";
import { Contract } from "@ethersproject/contracts";
import { useContractCall, useContractFunction } from "@usedapp/core";

import contractAbi from "../contracts/contractAbi.json";
import { myContractAddress as contractAddress } from "../contracts/contractAddress";

const simpleContractInterface = new ethers.utils.Interface(contractAbi);
const contract = new Contract(contractAddress, simpleContractInterface);

export function useTokenBalance(account) {
  const [tokenBalance] =
    useContractCall(
      account && {
        abi: simpleContractInterface,
        address: contractAddress,
        method: "balanceOf",
        args: [account],
      }
    ) ?? []; //the double question mark syntax (known formally by its very catchy name "Nullish coalescing operator"), if the left-hand side operand is null or undefined, it will return the right-hand operand, so if our useContractCall is undefined, the count variable we destructure will be undefined (since the right-hand operand is an empty array).
  return tokenBalance;
}

export function useContractMethod(methodName) {
  const { state, send } = useContractFunction(contract, methodName, {});
  return { state, send };
}
