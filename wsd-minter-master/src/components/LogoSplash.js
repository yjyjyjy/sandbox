import { Image } from "@chakra-ui/image";
import wsdlogo from "../images/WSD_Logo-DefaultWhite.png";
import { Box, Center, VStack } from "@chakra-ui/layout";
import { Progress } from "@chakra-ui/react";

export default function LogoSplash() {
  return (
    <>
      <Center height='100vh' width='100%'>
        <VStack>
          <Image src={wsdlogo} alt='wallstreetdads logo loader' maxHeight='420px' padding='10px' />
          <Box width='300px'>
            <Progress size='sm' isIndeterminate colorScheme='orange' />
          </Box>
        </VStack>
      </Center>
    </>
  );
}
