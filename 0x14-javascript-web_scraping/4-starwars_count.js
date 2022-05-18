#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;
let counter = 0;
const person = '/18/';
// Make a reques
axios.get(argv[2])
  .then(function (response) {
    for (const film in response.data.results) {
      for (const line in response.data.results[film].characters) {
        if (response.data.results[film].characters[line].includes(person)) {
          counter = counter + 1;
        }
      }
    }
    console.log(counter);
  }).catch(function (error) {
    // handle error
    console.log(error);
  });
