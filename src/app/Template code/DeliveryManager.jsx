import DeliverySummary from "./DeliverySummary";

export default function DeliveryManager({ data }) {
  const delivery = {
    Name: "weedsale",
    Time: "12pm",
    Address: "address",
    Items: ["corn", "soybeans"]
  };

  return (
    <div>
      <h1>
        This is a DeliveryManager of. Group ID: {data.GroupID}
        This is the delivery: {delivery.Name};
      </h1>
      <DeliverySummary data={delivery} />
    </div>
  );
}
