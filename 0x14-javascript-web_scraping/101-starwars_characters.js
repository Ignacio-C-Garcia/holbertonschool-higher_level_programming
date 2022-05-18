#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;
// Make a reques
function printer()
{
axios.get(`https://swapi-api.hbtn.io/api/films/${argv[2]}/`).then(function (response) { response.data.characters.forEach(myFunction) });
}
async function myFunction (url) {
await  new Promise(resolve => {
axios.get(url).then(function (response) {
    console.log(response.data.name);
  });
})}
printer();
