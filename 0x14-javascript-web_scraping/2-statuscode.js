#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;

// Make a request for a user with a given ID
axios.get(argv[2])
  .then(function (response) {
    // handle success
    console.log('code:', response.status);
  })
