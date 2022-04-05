#!/usr/bin/node
fs = require('fs');
const buff = Buffer.alloc(1024);
const buff2 = Buffer.alloc(1024);
let xd;
let xd2;
fs.open(process.argv[2], 'r', (err, fd) => {
  fs.read(fd, buff, 0, 1024, 0, (err, bytes, buff) => {
    xd = buff.toString();

    fs.open(process.argv[3], 'r', (err, fd2) => {
      fs.read(fd2, buff2, 0, (err, bytes, buff2) => { xd2 = buff2.toString(); });
    });
  });
  console.log(xd2 + xd);
});
