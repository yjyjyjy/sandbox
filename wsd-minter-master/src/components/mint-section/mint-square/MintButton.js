import { useEthers } from "@usedapp/core";
import { useState } from "react";
import { Box, Text, Button, Center } from "@chakra-ui/react";
import { useContractMethod } from "../../../hooks";
import { utils } from "ethers";
import {
  NumberInput,
  NumberInputField,
  NumberInputStepper,
  NumberIncrementStepper,
  NumberDecrementStepper,
} from "@chakra-ui/react";
import { Spinner } from "@chakra-ui/react";

import { Slider, SliderTrack, SliderFilledTrack, SliderThumb } from "@chakra-ui/slider";
import { HStack } from "@chakra-ui/layout";

import { Image } from "@chakra-ui/react";
import { Tooltip } from "@chakra-ui/react";

import Preload from "react-preload";
import minivan from "../../../images/minivan-slider.png";
//import minivanplaceholder from "../../../images/minivan-placeholder.png";

import { mintPrice } from "../../../contracts/mintPrice";

export default function MintButton() {
  const { account } = useEthers();
  const { state: mintState, send: mint } = useContractMethod("mint");
  //const { notifications } = useNotifications();
  //console.log( " {notifications}",notifications[0].transaction.hash)
  const [input, setInput] = useState(7);

  const images = [minivan];

  function handleSetCount() {
    const _count = parseInt(input);
    console.log(_count);
    if (_count) {
      mint(account, _count, {
        value: utils.parseEther((mintPrice * input).toString()),
      }); //calling the mint here! arguments and a config object at end for value wow read comments here https://dev.to/jacobedawson/send-react-web3-dapp-transactions-via-metamask-2b8n
    }
  }

  function handleInput(valueAsString) {
    setInput(valueAsString);
  }

  return (
    <Box
      width={["330px", "460px"]}
      height={["310px", "310px"]}
      alignItems='center'
      background='steelblue.900'
      borderRadius='xl'
      p='15px'
    >
      <Tooltip
        hasArrow
        label='Maximum of 20 each mint so other Wall Street Dads can have a chance to get theirs!'
        bg='neutral.500'
        placement='top'
      >
        <Center>
          <NumberInput
            size='lg'
            maxW='77px'
            min={1}
            max={20}
            my={2}
            value={input}
            onChange={handleInput}
            allowMouseWheel
            errorBorderColor='red.500'
            focusBorderColor='gold.500'
            inputMode='numeric'
            precision={0}
            aria-label='number of wallstreetdads to mint'
          >
            <NumberInputField color='white' />
            <NumberInputStepper>
              <NumberIncrementStepper color='white' />
              <NumberDecrementStepper color='white' />
            </NumberInputStepper>
          </NumberInput>
        </Center>
      </Tooltip>

      <Slider
        min={1}
        max={20}
        focusThumbOnChange={false}
        value={input}
        onChange={handleInput}
        aria-label='number of wallstreetdads to mint'
        my={12}
      >
        <SliderTrack>
          <SliderFilledTrack bg='gold.500' />
        </SliderTrack>
        <Preload
          loadingIndicator={<Image src={minivan} size='100%' alt='number to mint wallstreetdads' />}
          images={images}
          resolveOnError={false}
          mountChildren={true}
        >
          <SliderThumb bg='transparent' shadow='0' children={input} boxSize={["100px", "100px", "120px"]}>
            {/* content to be rendered once loading is complete */}
            {/**   {/*    <Box height={["45px", "45px", "55px"]} width={["100px", "100px", "120px"]}></Box> */}
            <Image src={minivan} size='100%' alt='number to mint wallstreetdads' />
          </SliderThumb>
        </Preload>
      </Slider>

      {/* <Tooltip hasArrow fontSize="lg" label={`YOLO! right? ..right? should I ask my wife's boyfriend?!?`} bg='neutral.500' placement='bottom'> cannot do tool tip because after metamask is closed it returns the focus to the button click and shows the tooltip again*/}

      {/* IMPORTANT to ENABLE BACK MINTING set disabled={!account}   */}
      {/* IMPORTANT to DISABLE MINTING BUTTON set disabled={true}   */}
      <Button
        disabled={true}
        bgColor='gold.500'
        color='steelblue.900'
        border='1px solid transparent'
        _hover={{
          border: "1px",
          borderStyle: "solid",
          borderColor: "steelblue.100",
          backgroundColor: "gold.100",
        }}
        _focus={{ boxShadow: "none" }}
        variant='solid'
        size='lg'
        isFullWidth
        onClick={handleSetCount}
        mt={0}
        mb={8}
      >
        Mint {input} Wall Street Dads!
      </Button>

      {!account ? (
        <Center>
          {/* <Text textStyle='normalbody' fontSize='md'>
                To Start Minting, Connect to MetaMask First.
              </Text> */}
          <Text textStyle='normalbody' fontSize='md'>
            Minting is Not Enabled Yet.
          </Text>
        </Center>
      ) : mintState.status === "Mining" ? (
        <>
          <Center>
            <HStack>
              <Spinner thickness='8px' speed='0.65s' emptyColor='steelblue.100' color='gold.500' size='md' />
              <Text textStyle='normalbody' fontSize='md'>
                Miners hard at work making your WSD!
              </Text>
            </HStack>
          </Center>
        </>
      ) : (
        <Center>
          {/* <Text textStyle='normalbody' fontSize='md'>
              Your Wallet Is Connected, You Can Mint.
            </Text> */}
          <Text textStyle='normalbody' fontSize='md'>
            Minting is Not Enabled Yet.
          </Text>
        </Center>
      )}

      {/* None,Mining, Success, Fail, Exception */}
    </Box>
  );
}
