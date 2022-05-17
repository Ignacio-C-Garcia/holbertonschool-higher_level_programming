#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;
const fs = require('fs');
// Make a reques
axios.get(`https://swapi-api.hbtn.io/api/films/${argv[2]}/`).then(function (response) {
	response.data.characters.forEach(myFunction)

}).catch(function (error) {
  // handle error
  console.log(error);
});
function myFunction(url) {
  axios.get(url).then(function (response) {
	console.log(response.data.name);
});
}
