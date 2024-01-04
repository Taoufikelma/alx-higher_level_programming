#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url)
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error(`Error: ${response.status} - ${response.statusText}`);
    }
  })
  .then(movie => {
    if (movie.episode_id === parseInt(movieId)) {
      console.log(movie.title);
    } else {
      console.log(`No movie found with ID ${movieId}`);
    }
  })
  .catch(error => {
    console.error(error.message);
  });
