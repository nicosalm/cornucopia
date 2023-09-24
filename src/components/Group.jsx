import ChartTabs from "./ChartTabs";
import DeliveryManager from "./DeliveryManager";
import React, { useState } from "react";
export default function Group(group) {
  const [state, setState] = useState(group);
  return (
    <div>
      <h1 className="text-6xl font-bold p-10" style={{ textAlign: "center" }}>Farmers Union</h1>
      {console.log("Group")}
      <ChartTabs />
      <DeliveryManager data={group} />
    </div>
  );
}