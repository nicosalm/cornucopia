export default function GroupPreview({ data, func }) {
  return (
    <div>
      <h1> this is a group preview of {data}</h1>
      <h1> rerender GroupDashboard after join or leave </h1>
      <button onClick={func}> rerender! </button>
    </div>
  );
}
