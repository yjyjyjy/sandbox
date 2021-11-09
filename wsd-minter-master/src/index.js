import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { DAppProvider } from "@usedapp/core";

import { ChakraProvider } from "@chakra-ui/react";
import theme from "./theme";



ReactDOM.render(
  <React.StrictMode>
    <ChakraProvider theme={theme}>
      <DAppProvider config={{}}>
        <App />
      </DAppProvider>
    </ChakraProvider>
  </React.StrictMode>,
  document.getElementById("root")
);
