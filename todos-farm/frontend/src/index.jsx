import { render } from "react-dom";
import { ChakraProps, ChakraProvider } from "@chakra-ui/react";

import Header from "./components/Header";

function App() {
  return (
    <ChakraProvider>
      <Header />
    </ChakraProvider>
  );
}

const rootElement = document.getElementById("root");
render(<App />, rootElement);