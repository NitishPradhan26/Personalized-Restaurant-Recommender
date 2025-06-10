import "./App.css";
import React, { useContext, useState } from "react";
import {
  Container,
  Row,
  Col,
  Button,
  Alert,
  Breadcrumb,
  Card,
  Form,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { ListContext } from "./Context";
import bakery from "./images/bakery.jpg";
import chicken from "./images/chicken.jpg";
import fries from "./images/fries.jpg";
import beef from "./images/beef.jpg";
import pork from "./images/pork.jpg";
import rice from "./images/rice.jpg";
import lamb from "./images/lamb.jpg";
import vegetarian from "./images/salad.jpg";
import sandwich from "./images/sandwich.jpg";
import dessert from "./images/dessert.jpg";
import poutine from "./images/poutine.jpg";
import fastfood from "./images/fastfood.jpg";
import burger from "./images/burger.jpg";
import seafood from "./images/seafood.jpg";
import pizza from "./images/pizza.jpg";
import breakfast from "./images/breakfast.jpg";
import coffee from "./images/coffee.jpg";
import alcohol from "./images/alcohol.jpg";
import noodles from "./images/noodles.jpg";
import pubfood from "./images/pubfood.jpg";
import indian from "./images/indian.jpg";
import italian from "./images/italian.jpg";
import barbecue from "./images/barbecue.jpg";
import chinese from "./images/chinese.jpg";
import vietnamese from "./images/vietnamese.jpg";
import japanese from "./images/japanese.jpg";
import mexican from "./images/mexican.jpg";
import sushi from "./images/sushi.jpg";
import mediterranean from "./images/mediterranean.jpg";
import sausage from "./images/sausage.jpg";
import middle from "./images/middleeastern.jpg";
import convenience from "./images/convenience.jpg";
import steak from "./images/steak.jpg";
import korean from "./images/korean.jpg";
import thai from "./images/thai.jpg";
import soup from "./images/soup.jpg";
import gluten from "./images/gluten.jpg";
import popcorn from "./images/popcorn.jpg";
import bubble from "./images/bubbletea.jpg";
import french from "./images/french.jpg";
import spanish from "./images/spanish.jpg";
import pet from "./images/pet.jpg";
import general from "./images/general.jpg";

const imageMap = {
  Chicken: chicken,
  Fries: fries,
  Beef: beef,
  Pork: pork,
  Rice: rice,
  Lamb: lamb,
  Vegetarian: vegetarian,
  "Sandwiches & Subs": sandwich,
  Desserts: dessert,
  Canadian: poutine,
  "Fast Food": fastfood,
  Burgers: burger,
  Seafood: seafood,
  Healthy: vegetarian,
  Pizza: pizza,
  "Breakfast & Brunch": breakfast,
  "Coffee/Tea": coffee,
  Alcohol: alcohol,
  Noodles: noodles,
  "Pub Food": pubfood,
  Indian: indian,
  Italian: italian,
  Bakery: bakery,
  Barbecue: barbecue,
  Chinese: chinese,
  Vietnamese: vietnamese,
  Japanese: japanese,
  Tacos: mexican,
  Sushi: sushi,
  Mediterranean: mediterranean,
  "Hot Dogs & Sausages": sausage,
  "Middle Eastern": middle,
  Convenience: convenience,
  Mexican: mexican,
  Steakhouse: steak,
  Halal: general,
  Korean: korean,
  Thai: thai,
  Soup: soup,
  "Gluten Free": gluten,
  Popcorn: popcorn,
  "Pet Food": pet,
  "Bubble Tea": bubble,
  French: french,
  African: general,
  "Latin American": general,
  "Haute Cuisine": general,
  Ethiopian: general,
  Caribbean: general,
  Filipino: general,
  Spanish: spanish,
  Butcher: general,
  Kosher: general,
  German: general,
};

function Results() {
  const { response, clearResponse } = useContext(ListContext);
  console.log(response);

  return (
    <div className="App">
      <header className="App-header">
        <button className="customed-btn" onClick={clearResponse}>
          Back to Homepage
        </button>
        <Row>{sortCustomerCuisines(response["Customers"][0])}</Row>

        <Row>
          <p>These Are the Restaurants From Your Tastes</p>
        </Row>
        <Row>
          {Object.keys(response["Restaurants"]).map((key1) => {
            return (
              <Col>
                <Card style={{ color: "black" }}>
                  {sortCuisinesInfoCard(response["Restaurants"][key1])}
                </Card>
              </Col>
            );
          })}
        </Row>
        <br />
        <Row>
          <p>These Are the Restaurants From You May Like</p>
          <br />
          <p>Recommended From 10M Orders Data Similarity Matrix!</p>
        </Row>
        <Row>
          {Object.keys(response["Varied_Restuarnts"]).map((key1) => {
            return (
              <Col>
                <Card style={{ color: "black" }}>
                  {sortCuisinesInfoCard(response["Varied_Restuarnts"][key1])}
                </Card>
              </Col>
            );
          })}
        </Row>
      </header>
    </div>
  );
}

function capitalizeWords(str) {
  return str.replace(/\b\w/g, function (l) {
    return l.toUpperCase();
  });
}

function sortCustomerCuisines(arr) {
  const sortObjByValues = (obj) => {
    const entries = Object.entries(obj.top_5);
    entries.sort((a, b) => b[1] - a[1]);
    return Object.fromEntries(entries);
  };

  const sortedObj = sortObjByValues(arr);

  const toPercentage = (value) => {
    return (value * 100).toFixed(2) + "%";
  };

  return (
    <div>
      <p>Your Taste Profile Is Here:</p>
      <div>
        {Object.entries(sortedObj).map(([key, value]) => (
          <div key={key}>
            {key}: {toPercentage(value)}
          </div>
        ))}
      </div>
    </div>
  );
}

function sortCuisinesInfoCard(arr) {
  const sortObjByValues = (obj) => {
    const entries = Object.entries(obj.top_5);
    entries.sort((a, b) => b[1] - a[1]);
    return Object.fromEntries(entries);
  };

  const sortedObj = sortObjByValues(arr);
  const firstKey = Object.keys(sortedObj)[0];
  const toPercentage = (value) => {
    return (value * 100).toFixed(2) + "%";
  };

  return (
    <div>
      <Card.Img src={imageMap[firstKey]} />
      <Card.Title>{capitalizeWords(arr["short_name"])}</Card.Title>

      <Card.Text className="card-text">
        Similarity: {toPercentage(arr["adjusted_score"])}
        <br />
        Restaurant Rating: {arr["restaurant_rating"]}
        <br />
        <br />
        {Object.entries(sortedObj).map(([key, value]) => (
          <div key={key}>
            {key}: {toPercentage(value)}
          </div>
        ))}
      </Card.Text>
    </div>
  );
}

export default Results;
