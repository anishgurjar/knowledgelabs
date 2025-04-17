import PetCard from './PetCard';
import './App.css'
import { useState } from 'react';

function App() {

  const [petContent, setPetContent] = useState([]);
  
  const addPets = () => {
    let pets = [
      {
        pet_name: "Milo",
        pet_image: "https://images.dog.ceo/breeds/retriever-golden/n02099601_3004.jpg",
        pet_description: "Loves belly rubs and loud barks"
      },
      {
        pet_name: "Luna",
        pet_image: "https://images.dog.ceo/breeds/husky/n02110185_14673.jpg",
        pet_description: "Runs in circles when excited"
      },
      {
        pet_name: "Rocky",
        pet_image: "https://images.dog.ceo/breeds/terrier-border/n02093754_3800.jpg",
        pet_description: "Will do tricks for treats"
      },
      {
        pet_name: "Daisy",
        pet_image: "https://images.dog.ceo/breeds/pug/n02110958_15626.jpg",
        pet_description: "Sleeps in the weirdest positions"
      },
      {
        pet_name: "Zeus",
        pet_image: "https://images.dog.ceo/breeds/great-dane/n02109047_2395.jpg",
        pet_description: "Thinks he's a lap dog"
      }
    ];

  const randomIndex = Math.floor(Math.random() * 5);
  const randomPet = pets[randomIndex];
  setPetContent(prevPets => [...prevPets, randomPet]);
  }

  return (
    <>
      <button onClick={addPets}>Add Pet</button>
      {petContent.map((pet) => (
        <PetCard  pet_name={pet.pet_name}
        pet_image={pet.pet_image}
        pet_description={pet.pet_description}
      />
      ))}
    </>
  )
}

export default App;
