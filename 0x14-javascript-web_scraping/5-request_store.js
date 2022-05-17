#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;
const fs = require('fs');
// Make a reques
axios.get(argv[2]).then(function (response) {
  
fs.writeFile(argv[3], response.data, { encoding: 'utf8' }, (err, data) => {
  if (err) {
    console.error(err);
  }
});

}).catch(function (error) {
    // handle error
    console.log(error);
  });
