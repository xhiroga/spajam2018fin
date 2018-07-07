import axios from "axios";
import { W3WKey } from "react-native-dotenv";

const w3wClient = axios.create({
  baseURL: "https://api.what3words.com/v2",
  timeout: 2000,
  headers: {"X-Api-Key": W3WKey}
});

export {
  w3wClient
};