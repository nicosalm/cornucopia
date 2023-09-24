import ChartTabs from "./ChartTabs";
import DeliveryManager from "./DeliveryManager";
import React, { useState } from "react";

export default function Group(group) {
  const [state, setState] = useState(group);

  const [formData, setFormData] = useState([
    { owner: "nico", crop: "corn", units: 30 },
    { owner: "lee", crop: "wheat", units: 20 },
    { owner: "jameson", crop: "barley", units: 10 },
  ]);

  const handleInputChange = ({ owner, crop, units }) => {
    setFormData([...formData, { owner, crop, units }]);
  };
  const handleContribution = (e) => {
    e.preventDefault();
    setFormData([...formData, { owner: "nico", crop: e.target.value, units: 30 }]);
  };

  return (
    <form onSubmit={handleContribution}>
      <div>
        {console.log(
          `${formData.deliveryName} ${formData.date} ${formData.location}`
        )}
      </div>

      <div>
        <div>
          <h4>Choose your crops to add or sell: </h4>
          <div>
            <select onChange={handleInputChange} placeholder="Crops">
              <option>corn</option>
              <option>wheat</option>
              <option>barley</option>
            </select>
          </div>

          <button type="submit">Contribute</button>
        </div>
      </div>
    </form>
  );
}
