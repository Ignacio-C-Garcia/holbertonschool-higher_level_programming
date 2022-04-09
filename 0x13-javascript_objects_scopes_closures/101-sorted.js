#!/usr/bin/node
const dict = require('./101-data').dict;
const sorted = {};
Object.values(dict).forEach(function (index) { sorted[index] = []; });
Object.keys(dict).forEach(key => sorted[dict[key]].push(key));
console.log(sorted);
