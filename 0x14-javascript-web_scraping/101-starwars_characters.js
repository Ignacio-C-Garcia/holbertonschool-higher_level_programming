#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;
// Make a reques
axios.get(`https://swapi-api.hbtn.io/api/films/${argv[2]}/`).then(function (response) {
  response.data.characters.forEach(myFunction);
}).catch(function (error) {
  // handle error
  console.log(error);
});
async function myFunction (url) {
  await axios.get(url).then(function (response) {
    console.log(response.data.name);
  });
}
