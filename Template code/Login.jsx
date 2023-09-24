import GroupDashboard from "./GroupDashboard";

export default function Login() {
  // Create user object/request from db
  const user = { ID: "12234" , Location: []};
  //After login is succesful:
  return (
    <div>
      <h1> Login Page with userID: {user.ID} </h1>
      <GroupDashboard userID={user} />
    </div>
  );
}
