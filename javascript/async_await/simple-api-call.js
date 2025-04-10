import axios from "axios";

async function getData() {
  try {
    const res = await axios.get('https://dog.ceo/api/breeds/image/random');
    console.log(res.data);
  } catch (err) {
    console.error('Error:', err.message);
  }
}

getData();
