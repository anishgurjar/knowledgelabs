import './App.css';

function App() {
  
  return <>
    <Post name={"Anish"} isPost={true}/>
    <Post name={"Amaya"} isPost={false}/>
  </>
}

function Post({name, isPost}) {
  return (
    <div className="post">
      <img src="https://media.licdn.com/dms/image/v2/D5603AQF6Q-I8biSPXA/profile-displayphoto-shrink_200_200/B56ZTiaP.7HoAY-/0/1738965320735?e=1750291200&v=beta&t=2Jrj9QaV3yBfiyHc0GcpiuEsrx5eiNUUSZlyU_BvSv4" alt="Profile" className="profile-photo" />
      <div className="post-content">
        <h2 className="post-title">{isPost ? "My First Post" : "My First Memo"}</h2>
        <p className="post-text">{isPost ? `Hello, my name is ${name}! This is my first post.` : `Hello, my name is ${name}! This is my first memo.`}</p>
      </div>
    </div>
  );
}

export default App;