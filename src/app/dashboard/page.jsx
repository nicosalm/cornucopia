"use client";

import { useState } from "react";
import GroupCard from "./GroupCard";

export default function Dashboard({ user }) {
  
  function rerenderDashboard() {
    console.log("Rerendering dashboard");
    setGroups(true);
  }
  
  
  
  
  // Create/ fetch group object
  let group1 = {
    _id: "1",
    user_ids: ["1", "11", "111"],
    crops: ["corn"],
    location: { lat: "1", lon: "1"}
  };
  
  let group2 = {
    _id: "2",
    user_ids: ["2", "22", "222"],
    crops: ["beans"],
    location: { lat: "2", lon: "2" }
  };
  
  let group3 = {
    _id: "3",
    user_ids: ["3", "33", "333"],
    crops: ["wheat", "barley"],
    location: { lat: "3", lon: "3"}
  };
  
  // TODO this is dummy data; replace please
  const groupList = [
    group1,
    group2,
    group3,
    group1,
    group2,
    group3,
    group1,
    group1,
  ];
  const [groups, setGroups] = useState(groupList);
  // setGroups(getGroupsAssociatedWithUser(user._id));

  return (
    <div className="m-4 p-4 justify-center">
      <h1 className="text-xl font-bold p-4">My Groups</h1>
      <div className="flex flex-wrap">
          { groups.map((gr, idx) => <GroupCard group={gr} key={idx} func = {rerenderDashboard}/> ) }        
          <div className="card-border text-center rounded-lg p-6 m-4 bg-green-800 hover:bg-green-600 transition-colors">
            New group
          </div>
      </div>
    </div>
  );
}
