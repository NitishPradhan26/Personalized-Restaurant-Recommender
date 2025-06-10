import React, { useState, useContext } from "react";
import {
  Container,
  Button,
  Collapse,
  Alert,
  Table,
  Row,
  Col,
  Card,
  Form,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import ButtonCollapse from "./ButtonCollapse";
import { ListContext } from "./Context";
import "./App.css";

function CForm() {
  const buttonStyle = { backgroundColor: "#BF6336", border: "none" };
  const [open, setOpen] = useState(false);
  const { list, addItem } = useContext(ListContext);
  console.log(list);
  // const japanese = [
  //   "Japanese",
  //   "ramen",
  //   "sashimi",
  //   "teriyaki",
  //   "katsu",
  //   "tempura",
  //   "edamame",
  //   "bento",
  // ];
  // const mediterranean = [
  //   "Mediterranean",
  //   "pita",
  //   "damascus",
  //   "greek",
  //   "greece",
  //   "briam",
  //   "taramasalata",
  //   "opa",
  // ];
  // const indian = [
  //   "Indian",
  //   "naan",
  //   "samosa",
  //   "masala",
  //   "aloo",
  //   "paneer",
  //   "biryani",
  // ];
  // const italian = [
  //   "Italian",
  //   "pasta",
  //   "spaghetti",
  //   "penne",
  //   "fettuccini",
  //   "lasagna",
  //   "lasagne",
  //   "linguini",
  //   "ravioli",
  //   "tortellini",
  //   "meatball",
  //   "canoli",
  // ];
  // const chinese = ["Chinese", "hot pot", "wonton", "cantonese", "mein"];
  // const vietnamese = ["Vietnamese", "pho", "viet", "bun cha", "ca kho to"];
  // const mexican = [
  //   "Mexican",
  //   "chilaquiles",
  //   "burrito",
  //   "nacho",
  //   "quesadilla",
  //   "queso",
  // ];
  // const korean = [
  //   "Korean",
  //   "kimchi",
  //   "bulgogi",
  //   "bibimbap",
  //   "tteokbokki",
  //   "jjambbong",
  //   "doenjang",
  // ];
  // const thai = ["Thai", "tom yum goong", "green curry"];
  // const french = [
  //   "French",
  //   "foie gras",
  //   "coq au vin",
  //   "cassoulet",
  //   "baguette",
  //   "croissants",
  //   "gougeres",
  //   "cajun & creole",
  // ];
  // const african = [
  //   "African",
  //   "pap en vleis",
  //   "shisa nyama",
  //   "bunny chow",
  //   "koshari",
  // ];
  // const latinAmerican = [
  //   "Latin",
  //   "asado",
  //   "saltena",
  //   "feijoada",
  //   "empanada",
  //   "bandeja paisa",
  //   "gallo pinto",
  //   "ropa vieja",
  //   "mangu",
  //   "encebollado",
  //   "pupusas",
  //   "pepian",
  //   "peruvian",
  // ];
  // const ethiopian = ["Ethiopian", "tibs", "kitfo", "beyainatu", "fuul"];
  // const caribbean = ["Caribbean", "jamaica", "barbados", "bahamas"];
  // const filipino = ["Filipino", "adobo", "lechon", "sisig", "bulalo"];
  // const spanish = [
  //   "Spanish",
  //   "paella valenciana",
  //   "patatas bravas",
  //   "gazpacho",
  //   "pimientos de padron",
  //   "jamon",
  //   "tapas",
  // ];
  // const german = ["German", "schnitzel", "rouladen", "eintopf", "sauerbraten"];
  // const middleEastern = [
  //   "Middle Eastern",
  //   "falafel",
  //   "hummus",
  //   "shawarma",
  //   "baklava",
  //   "donair",
  // ];

  // const protein = ["Protein", "chicken", "fries", "beef", "pork"];

  const foodItems = [
    "Barbecue",
    "Burger",
    "Beer/Alcohol",
    "Bubble Tea",
    "Chinese Hotpot",
    "Fastfood Combo Meal",
    "Coffee/Tea",
    "Waffle",
    "Filipino",
    "Fried Rice",
    "Fried Chicken",
    "Fries",
    "Foie Gras (French Goose Liver)",
    "Ice Cream",
    "Indian Masala",
    "Korean Bulgogi",
    "Mashed Potato",
    "Mediterranean",
    "Mexican Burrito",
    "Muffin",
    "Noodles",
    "Pizza",
    "Pork Belly",
    "Popcorn",
    "Poutine",
    "Beef Stew",
    "Roasted Lamb",
    "Roti",
    "Sashimi",
    "Sausage",
    "Shawarma",
    "Shrimp/Crab/Lobster",
    "Spanish",
    "Spaghetti/Pasta",
    "Steak",
    "Japanese Teriyaki",
    "Thai Green Curry",
    "Tonkotsu Ramen",
    "Vegetable Salad",
    "Vietnamese Pho",
    "Wings",
    "Wonton",
  ];
  return (
    <div
    //     style={{
    //           margin-top: "5px",
    //           margin-bottom: "5px",
    // margin-right: "5px",
    // margin-left: "5px",
    //     }}
    >
      <Row>
        {/* <Col>
          <Row>
            <ButtonCollapse cusine={japanese} />
          </Row>

          <Row>
            <ButtonCollapse cusine={mediterranean} />
          </Row>

          <Row>
            <ButtonCollapse cusine={indian} />
          </Row>

          <Row>
            <ButtonCollapse cusine={italian} />
          </Row>

          <Row>
            <ButtonCollapse cusine={chinese} />
          </Row>

          <Row>
            <ButtonCollapse cusine={vietnamese} />
          </Row>

          <Row>
            <ButtonCollapse cusine={mexican} />
          </Row>

          <Row>
            <ButtonCollapse cusine={korean} />
          </Row>

          <Row>
            <ButtonCollapse cusine={thai} />
          </Row>

          <Row>
            <ButtonCollapse cusine={french} />
          </Row>

          <Row>
            <ButtonCollapse cusine={african} />
          </Row>

          <Row>
            <ButtonCollapse cusine={latinAmerican} />
          </Row>

          <Row>
            <ButtonCollapse cusine={ethiopian} />
          </Row>

          <Row>
            <ButtonCollapse cusine={caribbean} />
          </Row>

          <Row>
            <ButtonCollapse cusine={filipino} />
          </Row>

          <Row>
            <ButtonCollapse cusine={spanish} />
          </Row>

          <Row>
            <ButtonCollapse cusine={german} />
          </Row>

          <Row>
            <ButtonCollapse cusine={middleEastern} />
          </Row>
        </Col> */}

        <Col>
          <Row>
            <div>
              {foodItems.map(function (item) {
                return (
                  <Button
                    variant="primary"
                    style={buttonStyle}
                    className="customed-btn"
                    key={item}
                    onClick={() => addItem(item)}
                  >
                    {item}
                  </Button>
                );
              })}
            </div>
          </Row>
        </Col>
      </Row>
    </div>
  );
}

export default CForm;
