import axios from "axios";
import { W3WKey } from "react-native-dotenv";

const w3wClient = axios.create({
  baseURL: "https://api.what3words.com/v2",
  timeout: 2000,
  headers: {"X-Api-Key": W3WKey}
});

const sawaraClient = axios.create({
  baseURL: "https://retravel.herokuapp.com/",
  timout: 5000,
})

export {
  w3wClient,
  sawaraClient
};