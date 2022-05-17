#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;

// Make a reques
axios.get(argv[2])
  .then(function (response) {
    // handle success
    console.log('code:', response.status);
  }).catch(function (error) {
    // handle error
    console.log('code:', error.response.status);
  })
