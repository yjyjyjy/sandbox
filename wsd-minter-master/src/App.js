import React from "react";
import { Suspense } from "react";

import { Box, Flex } from "@chakra-ui/layout";

import LogoSplash from "./components/LogoSplash";

const Layout = React.lazy(() => import("./components/Layout"));

const MintSection = React.lazy(() => import("./components/mint-section/MintSection"));

function App() {
  return (
    <>
      <Box bg='steelblue.500' minHeight='100vh' overflow='hidden'>
        <Suspense fallback={<LogoSplash />}>
          <Layout>
            <Flex bgColor='steelblue.500' direction='column' align='center' maxW={{ xl: "1200px" }} mx='0 auto'>
              <MintSection />
            </Flex>
          </Layout>
        </Suspense>
      </Box>
    </>
  );
}

export default App;
