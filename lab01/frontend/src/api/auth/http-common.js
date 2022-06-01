import axios from 'axios';

export const AUTH_API = axios.create({
  baseURL: `http://localhost:8000/`,
  headers: {
    // Overwrite Axios's automatically set Content-Type
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
})