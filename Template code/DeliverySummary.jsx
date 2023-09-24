import Delivery from "./Delivery";

export default function DeliverySummary({ data }) {
  return (
    <div>
      <h1> This is a deliverysummary of {data.Name} </h1>
      <Delivery data={data} />
    </div>
  );
}
