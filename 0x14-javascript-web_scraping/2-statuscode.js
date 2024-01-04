#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url)
  .then(response => {
    console.log(`code: ${response.status}`);
  })
  .catch(error => {
    console.error(error.message);
  });
