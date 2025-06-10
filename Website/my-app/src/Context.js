import React, { createContext, useState } from "react";

export const ListContext = createContext();

const ListContextProvider = ({ children }) => {
  const [list, setList] = useState([]);
  const [orders, setOrders] = useState([]);
  const [response, setResponse] = useState(null);

  const addItem = (item) => {
    setList([...list, item]);
  };

  const removeItem = (index) => {
    setList((prevList) => {
      const newList = [...prevList];
      newList.splice(index, 1);
      return newList;
    });
  };

  const clearList = () => {
    setList([]);
  };

  const saveOrder = (date) => {
    const newOrder = {
      items: list,
      date, // get the current date in ISO 8601 format
    };
    setOrders([...orders, newOrder]);
    setList([]);
  };

  const clearOrder = () => {
    setOrders([]);
  };

  const getResponse = (data) => {
    setResponse(data);
  };
  const clearResponse = () => {
    setResponse(null);
  };
  return (
    <ListContext.Provider
      value={{
        list,
        addItem,
        clearList,
        removeItem,
        orders,
        saveOrder,
        clearOrder,
        response,
        getResponse,
        clearResponse,
      }}
    >
      {children}
    </ListContext.Provider>
  );
};

export default ListContextProvider;
