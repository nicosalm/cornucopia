export default function GroupPreview({ data, func }) {
console.log("Preview rendered");
    return (
      <div>
      {console.log("Render2")}
        <h1> this is a group preview of {data}</h1>
        <h1> rerender GroupDashboard after join or leave </h1>
        <button onClick={func}> rerender! </button>
      </div>
    );
  }