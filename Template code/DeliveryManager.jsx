import DeliverySummary from "./DeliverySummary";
import FarmMap from "./FarmMap";

export default function DeliveryManager({ data }) {
  const delivery = {
    Name: "weedsale",
    Time: "12pm",
    Location: "address",
    Items: ["corn", "soybeans"]
  };
  const farmLocations = [
    { lat: 51.5072, lng: -0.1276, name: "Farm 1" },
    { lat: 51.5151, lng: -0.1589, name: "Farm 2" },
    // ... other farm locat ions
];

const iconURL = "./src/app/assets/nico.png"; // Replace with your icon URL
  return (
    <div>
      <h1>
        Scheduled Drop-Offs:
      </h1>
      <FarmMap farmLocations={farmLocations} iconURL={iconURL}/>
      <DeliverySummary data={delivery} />
    </div>
  );
}
