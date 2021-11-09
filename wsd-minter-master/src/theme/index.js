import { extendTheme } from "@chakra-ui/react";
import { createBreakpoints } from "@chakra-ui/theme-tools";

const theme = extendTheme({
  //breakpoints: ["30em", "48em", "62em", "80em"],
  fonts: {
    heading: "Fira Sans Condensed",
    body: "Fira Sans Condensed",
    cursive: "Amatic SC", //tahu replacement
  },
  textStyles: {
    menuitems: {
      //semibold 600
      fontFamily: "heading",
      fontWeight: "600",
      fontSize: "lg",
      color: "white",
    },

    normalbody: {
      //light 300
      fontFamily: "body",
      fontWeight: "300",
      fontSize: "xl",
      color: "white",
    },

    emphasis: {
      //extrabold 800 italic
      fontFamily: "body",
      fontWeight: "800",
      fontSize: "xl",
      fontStyle: "italic",
      color: "white",
    },

    subheads: {
      fontFamily: "cursive",
      fontWeight: "700",
      fontSize: "6xl",
      color: "gold.500",
      textTransform: "uppercase",
      lineHeight: "110%",
    },
  },
  colors: {
    gold: {
      50: "#f1d334",
      100: "#f0d038",
      200: "#efcc3c",
      300: "#eec841",
      400: "#ecc347",
      500: "#eabd4e", // brandgold
      600: "#d3ac4b",
      700: "#cba64a",
      800: "#c7a44a",
      900: "#bb9b48", //darkgold
    },
    steelblue: {
      50: "#828695",
      100: "#797e8d",
      200: "#6e7485",
      300: "#62687b",
      400: "#545a6e",
      500: "#434A60", //brandsteelblue
      600: "#3d4357",
      700: "#383e50",
      800: "#34394a",
      900: "#303545",
    },
    neutral: {
      500: "#96825e", //neutral color
    },
    darkgray: {
      500: "#333333", //for text on white, use this instead of black
    },
  },
  // components: { Button: { baseStyle: { _focus: { boxShadow: "none", border: "none" } } } },//this only disables highlighting of selected components
});

const myBreakpoints = createBreakpoints({
  sm: "30em",
  md: "56em",
  lg: "62em",
  xl: "80em",
  "2xl": "96em",
});

theme.breakpoints = myBreakpoints;

export default theme;
