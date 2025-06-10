import React, { useContext } from "react";
import Submit from "./Submit";
import ClearButton from "./ClearButton";
import Items from "./Items";
import SaveOrder from "./SaveOrder";
import ListOrder from "./ListOrders";
import CForm from "./CForm";
import Results from "./Results";
import backgroundImage from "./images/background.jpg";
import "bootstrap/dist/css/bootstrap.min.css";
import { ListContext } from "./Context";
import { Image, Row, Col, Container } from "react-bootstrap";

function Homepage() {
  const { response } = useContext(ListContext);

  return (
    <div className="homepage">
      {!response && (
        <div
          style={{
            backgroundImage: `url(${backgroundImage})`,
            backgroundSize: "cover",
            backgroundRepeat: "repeat",
            backgroundPosition: "center center",
          }}
        >
          <div>
            <br />
            <br />
            <br />
          </div>
          <CForm />
          <br />
          <br />
          <br />
          <Row>
            <Col>
              <div className="item-list-box">
                <br />
                <div className="list-Col">
                  <Container style={{ height: "450px", overflowY: "scroll" }}>
                    <Items />
                  </Container>
                </div>
                <ClearButton />
                <SaveOrder />
              </div>
            </Col>

            <Col>
              <div className="item-list-box">
                <br />
                <Container style={{ height: "500px", overflowY: "scroll" }}>
                  <ListOrder />
                </Container>

                <Submit />
              </div>
            </Col>
          </Row>
          <div>
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
          </div>
        </div>
      )}
      {response && (
        <div>
          <Results />
        </div>
      )}
    </div>
  );
}

export default Homepage;
