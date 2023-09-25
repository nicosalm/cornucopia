import React, { useState } from 'react';

function Delivery(data) {
  const user = {
    crops: ["Tomato", "Lettuce"],
    quantity: {
      "Tomato": 40,
      "Lettuce": 30
    }
  }

  const deliveryItem = {
    name: "Gardener's Group Saturday Drop-Off",
    date: "2011-10-10",
    location: "Madison, WI",
    cropPrices: {
      "Tomato": 2.99,
      "Carrot": 1.49,
      "Lettuce": 0.99,
    },
    cropInventory: {
      "Tomato": 200,
      "Carrot": 300,
      "Lettuce": 400
    },
    users: [user, "Nico", "Lee"]
  }


  const [formData, setFormData] = useState({
    deliveryName: deliveryItem.name,
    date: deliveryItem.date,
    location: deliveryItem.location,
    cropPrices: deliveryItem.cropPrices,
    cropInventory: deliveryItem.cropInventory,
    userList: deliveryItem.users
  });

  const [currentUserCrops, setCurrentUserCrops] = useState({});
  const [joinedUsers, setJoinedUsers] = useState([]);

  const [isJoining, setIsJoining] = useState(false);

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleUserCropChange = (e) => {
    setCurrentUserCrops({
      ...currentUserCrops,
      [e.target.name]: e.target.value,
    });
  };

  const handleJoin = (e) => {
    e.preventDefault;
    setIsJoining(true);
  };

  const handleContribution = (e) => {
    e.preventDefault();
    // Upon submission, query database by adding number of crops into the delivery object. Reduce inventory
    // size
    const newDeliveryItem = {
      name: "Gardener's Group Saturday Drop-Off",
      date: "2011-10-10",
      location: "Madison, WI",
      cropPrices: {
        "Tomato": 2.99,
        "Carrot": 1.49,
        "Lettuce": 0.99,
      },
      cropInventory: {
        "Tomato": 240,
        "Carrot": 300,
        "Lettuce": 400
      },
      users: [user, "Nico", "Lee"]
    }
    setFormData(newDeliveryItem);
  };



  return (
    <form onSubmit={handleContribution}>
      <div>
        {console.log(`${formData.deliveryName} ${formData.date} ${formData.location}`)}
        <label>Delivery Name: </label>
        <input style = {{color :"black"}}type="text" name="deliveryName" value={formData.deliveryName} onChange={handleInputChange} />

        <label> Date: </label>
        <input style = {{color :"black"}}type="date" name="date" value={formData.date} onChange={handleInputChange} />

        <label> Location: </label>
        <input style = {{color :"black"}}type="text" name="location" value={formData.location} onChange={handleInputChange} />
      </div>
      <div>
        <h3>Crops and Prices</h3>
        {Object.entries(formData.cropPrices).map(([crop, price]) => (
          <ul key={crop}>
            <ul>Crop: {crop}  Amount: {formData.cropInventory[`${crop}`]} ${price}/lb</ul>
          </ul>
        ))}
      </div>
      <div>
      </div>

      <div style = {{containerType: "box", display:"flex"}}>  
        <button style= {{justifyContent:"center", alignContent:"center", color:"black", borderBlockColor:"black"}}  onClick={handleJoin}>Join</button>
        {isJoining && (
          <div>
            <h4>Choose your crops to add to the delivery: </h4>
              <div>
                <select onChange={handleUserCropChange} placeholder="Crops" style={{color:"black"}}>
                  {user.crops.map((crop, index)=> (
                    <option key = {index} value={crop}> {`        ${user.quantity[`${crop}`]}`} </option>
                  ))}
                </select>

              </div>
            
            <button type="submit">Contribute</button>
          </div>
        )}
      </div>
    </form>
  );
}
export default Delivery;

