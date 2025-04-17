import { useState } from "react";

const Post = ({username}) => {

    const [postState, setPostState] = useState({likeCount: 0, commentCount: 0});
    const updateLike = () => {
        setPostState((prev) => ({ ...prev, likeCount: prev.likeCount + 1 }));
    }
    const updateComment = () => {
        setPostState((prev) => ({...prev, commentCount: prev.commentCount + 1}))
    }

    return (
    <div style={styles.post}>
        <div style={styles.header}>
        <div style={styles.avatar}></div>
        <div>
            <div style={styles.username}>{username}</div>
            <div style={styles.timestamp}>Just now</div>
        </div>
        </div>
        <div style={styles.content}>
        <p>This is a sample post content. Replace this with your own state-driven content.</p>
        </div>
        <div style={styles.footer}>
        <button style={styles.button} onClick={updateLike}>
            <span role="img" aria-label="thumbs up">👍</span>
        </button>
        <span style={styles.count}>{postState.likeCount} Likes</span>
        <button style={styles.button} onClick={updateComment}>
            <span role="img" aria-label="comment">💬</span>
        </button>
        <span style={styles.count}>{postState.commentCount} Comments</span>
        </div>
    </div>
    );


};

const styles = {
  post: {
    maxWidth: '500px',
    margin: '20px auto',
    padding: '16px',
    borderRadius: '10px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
    backgroundColor: '#fff',
    fontFamily: 'sans-serif',
  },
  header: {
    display: 'flex',
    alignItems: 'center',
    marginBottom: '12px',
  },
  avatar: {
    width: '40px',
    height: '40px',
    borderRadius: '50%',
    backgroundColor: '#ccc',
    marginRight: '12px',
  },
  username: {
    fontWeight: 'bold',
    fontSize: '14px',
  },
  timestamp: {
    fontSize: '12px',
    color: '#777',
  },
  content: {
    fontSize: '15px',
    marginBottom: '16px',
  },
  footer: {
    display: 'flex',
    gap: '8px',
    alignItems: 'center',
  },
  button: {
    padding: '6px 12px',
    border: 'none',
    borderRadius: '4px',
    backgroundColor: '#007bff',
    color: '#fff',
    cursor: 'pointer',
  },
  count: {
    fontSize: '14px',
    color: '#555',
  },
};

export default Post;
