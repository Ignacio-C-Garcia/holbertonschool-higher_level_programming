#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;
let counter = 0;
person = 'https://swapi-api.hbtn.io/api/people/18/'
// Make a reques
axios.get(argv[2])
  .then(function (response) {
 let cosa = response.data.results[0].characters;
for (kk in response.data.results)
	if (response.data.results[kk].characters.includes(person)){
		counter = counter + 1;
		}
console.log(counter)
  }).catch(function (error) {
    // handle error
    console.log(error);
  });
