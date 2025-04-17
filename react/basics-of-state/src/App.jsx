import Post from "./Post";

function App() {
  const usernames = ["Anish", "John", "Doe", "Alice", "Bob"];
  
  return (
    <>
      {usernames.map((username) => (
        <Post username={username} />
      ))}
    </>
  );
}

export default App;
