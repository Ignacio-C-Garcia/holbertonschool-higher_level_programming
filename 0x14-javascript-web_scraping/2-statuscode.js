#!/usr/bin/node
const argv = require('process').argv;
const Request = require('request');
const request = new Request(argv[2], function (error, response, body) {
console.log('code: ', response.statusCode)
})
