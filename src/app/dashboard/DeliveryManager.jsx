import DeliverySummary from "./DeliverySummary";
import FarmMap from "./FarmMap";
import React, { useState} from "react";
export default function DeliveryManager({ data }) {
  // hardcoding data. Replace with db query
  const deliver = {
    Name: "weedsale",
    Time: "12pm",
    Location: [2021, 3041],
    Items: ["corn", "soybeans"]
  };
  const[delivery, setDelivery] = useState(deliver);
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

const iconURL = "./src/app/assets"; // Replace with your icon URL
  return (
    <div>
      <h1 id = "ScheduledDropOff">
        Scheduled Drop-Offs:
      </h1>
      <FarmMap farmLocations={farmLocations} iconURL={iconURL} setDelivery = {newDelivery}/>
      <DeliverySummary data={delivery} />
    </div>
  );
}
