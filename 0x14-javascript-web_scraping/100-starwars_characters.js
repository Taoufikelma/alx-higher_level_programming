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
    console.log(`Characters in ${movie.title}:`);
    return Promise.all(movie.characters.map(characterUrl => request(characterUrl)));
  })
  .then(responses => Promise.all(responses.map(response => response.json())))
  .then(characters => {
    characters.forEach(character => console.log(character.name));
  })
  .catch(error => {
    console.error(error.message);
  });
