import { useEffect, useState } from "react";
import GroupPreview from "./GroupPreview";
import Group from "./Group";

export default function GroupCard({group, func1, func2, isPreview}) {

  const { _id, user_ids, crops, location } = group;
  const { lat, lon } = location;

  const render = () => func2([isPreview, group]);

  return (
    <div>
    <div
      className="card card-border rounded-lg shadow-sm p-6 m-4 hover:bg-green-900 transition-colors"
      onClick= {render}
    >
      <p className="mb-4">
        ID: <span className="font-bold">{_id}</span>
      </p>
      <p className="mb-2">
        Members: <span className="font-bold">{user_ids.length}</span>
      </p>
      <p className="mb-2">
        Crops: <span className="font-bold">{crops.join(", ")}</span>
      </p>
      <p className="">
        Location: <span className="font-bold">{`(${lat}, ${lon})`}</span>
      </p>
      
    </div>
    <span>
    
    </span>
    </div>
  );
}
