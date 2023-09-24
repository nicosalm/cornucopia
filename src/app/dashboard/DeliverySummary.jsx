
import Delivery from "./Delivery";
import "./DeliverySummary.css";
import React, { useState, useEffect } from "react";


export default function DeliverySummary({ data }) {
  const delivery = {
    Name: "weedsale",
    Time: "12pm",
    Location: "address",
    Items: ["corn", "soybeans"]
  };
  const [display, setDisplay] = useState(true);
  function toggleDisplay(display){
    setDisplay(display? false :true);
  }
  return (
    <div >
      {display ? <button id = "delSummary" onClick={toggleDisplay}> 
      <p> {data.Name}</p> <p> {data.Time}</p> 
      <p> {`Lat: ${data.Location[0]} Long: ${data.Location[1]}`}</p> 
      <p> {...data.Items}</p>
      </button> :<Delivery data={delivery}/>} 
    </div> 
  );
}
