#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;

// Make a reques
axios.get('https://swapi-api.hbtn.io/api/films/'.concat(argv[2]))
  .then(function (response) {
    // handle success
    console.log(response.data.title);
  }).catch(function (error) {
    // handle error
	console.log()
  });
