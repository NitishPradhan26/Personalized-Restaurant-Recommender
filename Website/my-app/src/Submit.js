import React, { useContext, useState } from "react";
import { ListContext } from "./Context";
import "./App.css";

const Submit = () => {
  const { orders, getResponse, clearOrder } = useContext(ListContext);
  console.log(orders);

  const handleSubmit = async () => {
    try {
      console.log(orders);
      const res = await fetch("http://127.0.0.1:5000/reccomend", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(orders),
      });
      const data = await res.json();
      // console.log(typeof res);
      getResponse(data);
      clearOrder();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <button className="customed-btn" onClick={handleSubmit}>
        Skip the Effort!
      </button>
      {/* {response && (
        <div>
          <h2>Response:</h2>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )} */}
    </div>
  );
};

export default Submit;
