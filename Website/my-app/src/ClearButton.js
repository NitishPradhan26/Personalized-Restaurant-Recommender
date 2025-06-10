import React, { useContext } from "react";
import { ListContext } from "./Context";

const ClearButton = () => {
  const { list, clearList } = useContext(ListContext);

  const handleClear = () => {
    clearList();
  };

  return (
    <button className="customed-btn" onClick={handleClear}>
      Clear List
    </button>
  );
};

export default ClearButton;
