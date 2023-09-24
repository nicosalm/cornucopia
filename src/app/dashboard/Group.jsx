import DeliveryManager from "./DeliveryManager";
import React, { useState } from "react";
export default function Group(group) {
  const [state, setState] = useState(group);
  return (
    <div>
      <h1>
        {" "}
        This is a singular group component rendered. Group ID: {
          group.GroupID
        }{" "}
      </h1>
      <button onClick = {setState} > rerender Group.jsx </button>
      {console.log("Group")}
      <DeliveryManager data={group} />
    </div>
  );
}