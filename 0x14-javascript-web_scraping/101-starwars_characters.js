#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;
// Make a reques
async function getlist () {
  const response = await axios.get(`https://swapi-api.hbtn.io/api/films/${argv[2]}/`);

  for (const person in response.data.characters) {
    await axios.get(response.data.characters[person]).then(function (response2) {
      console.log(response2.data.name);
    }).catch(error => { console.log(error); });
  }
}
getlist();
