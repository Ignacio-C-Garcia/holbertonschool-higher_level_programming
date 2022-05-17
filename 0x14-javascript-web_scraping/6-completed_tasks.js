#!/usr/bin/node
const argv = require('process').argv;
const axios = require('axios').default;
// Make a reques
const dict = {};
axios.get('https://jsonplaceholder.typicode.com/users').then(function (response) {
  for (let size = 1; size <= response.data.length; size++) { dict[`${size}`] = 0; }
  axios.get(argv[2]).then(function (response2) {
    for (const index in response2.data) {
      if (response2.data[index].completed) {
        dict[response2.data[index].userId] = dict[response2.data[index].userId] + 1;
      }
    }
    console.log(dict);
  });
});
