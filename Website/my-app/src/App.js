import "./App.css";
import React, { useState } from "react";
import STFlogo from "./logo1.png";
import backgroundImage from "./images/background.jpg";
import { Image, Row, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import ListContextProvider from "./Context.js";
import Homepage from "./Homepage";

function App() {
  const barStyle = { backgroundColor: "white" };
  return (
    <div className="App">
      <div style={barStyle}>
        <Image
          src={STFlogo}
          width="388.4"
          height="167.6"
          className="d-inline-block align-top"
          alt="Your logo"
        />
      </div>

      <ListContextProvider>
        <Homepage />
      </ListContextProvider>
      {/* <Results /> */}
    </div>
  );
}

export default App;
