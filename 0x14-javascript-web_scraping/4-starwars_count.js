#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;
let counter = 0;
const person = 'https://swapi-api.hbtn.io/api/people/18/';
// Make a reques
axios.get(argv[2])
  .then(function (response) {
    for (const film in response.data.results) {
      if (response.data.results[film].characters.includes(person)) {
        counter = counter + 1;
      }
    }
    console.log(counter);
  }).catch(function (error) {
    // handle error
    console.log(error);
  });
