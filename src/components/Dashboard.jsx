"use client";

import { useState, useEffect } from "react";
import GroupCard from "@/components/GroupCard";
import Group from "@/components/Group";
import GroupPreview from "@/components/GroupPreview";

export default function Dashboard({ user }) {
  let prev = false;
  useEffect(() => {
    console.log(render.isPreview);
    if(render.isPreview === true){
        prev = true;
    }
  })
  function rerenderDashboard(group) {
    console.log("Rerendering dashboard");
    setGroups(...group);
  }
  const[render, setRender] = useState({
    isPreview: false,
    isRender: false,
    group: null
  }
  )
  
  function cardRenderer([preview, group]){
    console.log(`in render: ${preview}`);
    const newRender = {
      
      isPreview : preview,
      isRender: true,
      group: group
    }
    setRender(newRender);
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
    <div>
      <div className="m-4 p-16 text-center">
        <h1 className="text-6xl font-bold p-10">Connect</h1>
        <div className="flex flex-wrap">
            { groups.map((gr, idx) => <GroupCard group={gr} func1 = {rerenderDashboard} func2 = {cardRenderer} isPreview = {true}/>) }        
            <div className="card-border rounded-lg p-6 m-4 bg-green-800 hover:bg-green-600 transition-colors">
              New group
            </div>
        </div>
    </div>

    <div className="m-4 p-16 justify-center">
      <h1 className="text-6xl text-center font-bold p-10">My Groups</h1>
      <div className="flex flex-wrap">
          { groups.map((gr, idx) => <GroupCard group={gr} func1 = {rerenderDashboard} func2={cardRenderer} isPreview = {false}/>) }        

      </div>
    </div>
    {console.log("rendering")}
      { (render.isRender && render.isPreview === true) ? <GroupPreview data={render.group._id} func={rerenderDashboard} /> : null}
      { (render.isRender && !render.isPreview) ? <Group data={render.group} />:null}
    </div>
    
  );
}
