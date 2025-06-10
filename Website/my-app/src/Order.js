import React, { useContext } from "react";
import { ListContext } from "./Context";

const Order = ({ order }) => {
  return (
    <div className="list-Col">
      <p>Items: {order.items.join(", ")}</p>
      <p>Date: {order.date}</p>
    </div>
  );
};

export default Order;
