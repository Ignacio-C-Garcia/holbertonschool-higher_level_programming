#!/usr/bin/node
const fs = require('fs');
const argv = require('process').argv;
fs.writeFile(argv[2], argv[3], {encoding: "utf8"}, (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
});
