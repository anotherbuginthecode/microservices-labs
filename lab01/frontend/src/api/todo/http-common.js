import axios from 'axios';

export const TODO_API = axios.create({
  baseURL: `http://localhost:5000/`,
  headers: {
    // Overwrite Axios's automatically set Content-Type
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
})