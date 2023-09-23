import DeliveryManager from "./DeliveryManager";

export default function Group(group) {
  return (
    <div>
      <h1>
        {" "}
        This is a singular group component rendered. Group ID: {
          group.GroupID
        }{" "}
      </h1>
      <DeliveryManager data={group} />
    </div>
  );
}
