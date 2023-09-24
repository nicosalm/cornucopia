"use client";

import "./DeliveryManager.css";
import DeliverySummary from "./DeliverySummary";
import FarmMap from "./FarmMap";
import React, { useState} from "react";
  
export default function DeliveryManager({ data }) {
  
  // hardcoding data. Replace with db query
  const defaultDelivery = {
    Name: "Gardener's Group Saturday Drop-Off",
    Time: "12PM CST",
    Location: [2021, 3041],
    Items: ["Corn ", "Soybeans "]
  };
  
  const[delivery, setDelivery] = useState(defaultDelivery);
  function newDelivery(newLocation){
    setDelivery((delivery) => {
      return {...delivery, Location: newLocation}
    })
  }
  const farmLocations = [
    { lat: 51.5072, lng: -0.1276, name: "Farm 1" },
    { lat: 51.5151, lng: -0.1589, name: "Farm 2" },
    // ... other farm locat ions
];

const iconURL = "./src/assets/nico.png"; // Replace with your icon URL

  return (
    /* div flex container */
    <div className="flex flex-col items-center justify-center h-screen text-xl">
      <h1 id = "ScheduledDropOff" className="text-4xl mb-6">
        Scheduled Drop-Offs
      </h1>
      <FarmMap className="rounded-lg mt-4" farmLocations={farmLocations} iconURL={iconURL} setDelivery = {newDelivery} />
      <div className="bg-white p-6 rounded-lg shadow-lg bg-[radial-gradient(ellipse_at_bottom_left,_var(--tw-gradient-stops))] from-[#134E5E] to-[#71B280]">
        <DeliverySummary data = {delivery}/>
      </div>
      <div className="h-4"></div>
      <button className="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow"
        onClick={() => {
          setDelivery(defaultDelivery);
        }}>
          Add New Drop-Off
        </button>
    </div>
  );
}