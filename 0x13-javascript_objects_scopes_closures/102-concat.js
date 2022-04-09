#!/usr/bin/node
const fs = require('fs');
if (process.argv[4] !== undefined) {
  fs.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }

    fs.writeFile(process.argv[4], data, { flag: 'a' }, (err) => {
      if (err) {
        console.log(err);
      }
    });
  });
  fs.readFile(process.argv[3], 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      return;
    }

    fs.writeFile(process.argv[4], data2, { flag: 'a+' }, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
}
