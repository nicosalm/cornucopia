import GroupPreview from "./GroupPreview";
import Group from "./Group";
import React, { useState } from "react";

export default function ({ user }) {
  // Create/ fetch group object
  let group = {
    GroupID: "1234",
    Member: [user, "1234"],
    Crops: ["Corn"],
    Location: ["X:12345", "Y:12345"]
  };
  const groupList = ["Group1", "Group2", "Group3"];
  const [state, setState] = useState(groupList);
  // This method is to rerender the dashboard
  function rerenderDashboard() {
    console.log("Rerendering dashboard");
    setState(true);
  }

  return (
    // button on click
    <div>
      <h1> This is a groupdashboard with groups {group.GroupID} </h1>
      <h1> This is a GroupPreview of {group.GroupID} </h1>
      <GroupPreview data={group.GroupID} func={rerenderDashboard} />
      <h1> This is a Group displayed on click in groupdashboard </h1>
      <Group group={group} />
    </div>
  );
}
