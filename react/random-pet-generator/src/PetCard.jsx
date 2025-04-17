import { useState } from 'react';
import './App.css'

const PetCard = ({ pet_name, pet_image, pet_description }) => {

    const [petState, setPetState] = useState({
        up_votes: 0,
        down_votes: 0
    })

    const updateUpVotes = () => {
        setPetState((prev) => ({...prev, up_votes: prev.up_votes + 1}))
    }

    const updateDownVotes = () => {
        setPetState((prev) => ({...prev, down_votes: prev.down_votes + 1}))
    }

    return (
        <>
          <div className="pet-card">
            <img
              src={pet_image}
              className="pet-image"
              alt={pet_name}
            />
            <h2 className="pet-name">{pet_name}</h2>
            <p className="pet-description">
              {pet_description}
            </p>
            <div className="vote-buttons">
              <p>{petState.up_votes}</p>
              <button className="upvote" onClick={updateUpVotes}>👍 Upvote</button> 
              <p>{petState.down_votes}</p>
              <button className="downvote" onClick={updateDownVotes}>👎 Downvote</button>
            </div>
          </div>
        </>
      );      
}

export default PetCard;