import { Container, SimpleGrid, Image, Stack } from "@chakra-ui/react";

import MintSquare from "./MintSquare";

import { VStack, Text, Center, Button } from "@chakra-ui/react";
import joker from "../../images/carousel600.gif";
import { FaTwitter, FaDiscord } from "react-icons/fa";
import { Box } from "@chakra-ui/layout";

import Slide from "react-reveal/Slide";

export default function MintSection() {
  return (
    <>
      <VStack spacing={4}>
        <Slide bottom>
          <Text align='center' textStyle='subheads' id='minty' mb='20px'>
            Firing Up The Ole' Mint
          </Text>

          <Stack direction={["column", "column", "row"]} spacing={5}>
            <Button
              onClick={() => window.open("https://twitter.com/WallStreetDads", "_blank")}
              size='lg'
              colorScheme='twitter'
              leftIcon={<FaTwitter />}
              _focus={{ boxShadow: "none" }}
            >
              JOIN US ON TWITTER
            </Button>
            <Button
              onClick={() => window.open("https://discord.gg/wallstreetdads", "_blank")}
              size='lg'
              colorScheme='cyan'
              leftIcon={<FaDiscord />}
              _focus={{ boxShadow: "none" }}
            >
              JOIN US ON DISCORD
            </Button>
          </Stack>

          <Box textAlign='center'>
            <Text as='span' textStyle='emphasis' fontSize='x-large' maxWidth='43ch' align='center'>
              NOTE
            </Text>
            <Text as='span' textStyle='normalbody' fontSize='x-large' maxWidth='43ch' align='center'>
              : Minting is NOT enabled yet. Join our Discord to find out the launch date time!
            </Text>
          </Box>
        </Slide>

        <Container maxW={"1200px"} py={0} px={0}>
          <SimpleGrid columns={{ base: 1, md: 2 }} spacing={[2, 2, 2]}>
            <Container maxW={"600px"}>
              <Slide bottom>
                <Center>
                  <Image objectFit='contain' src={joker} alt='mintimage' my='10px' />
                </Center>
              </Slide>
            </Container>

            <Container maxW={"600px"}>
              <Slide bottom>
                <Center>
                  <MintSquare />
                </Center>
              </Slide>
            </Container>
          </SimpleGrid>
        </Container>
      </VStack>
      <Box visibility='hidden' my='30px'>
        -
      </Box>
    </>
  );
}
