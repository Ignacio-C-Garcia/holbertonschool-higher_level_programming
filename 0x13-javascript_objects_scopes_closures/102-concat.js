#!/usr/bin/node
fs = require('fs');
const buff = Buffer.alloc(1024);
const buff2 = Buffer.alloc(1024);
fs.open(process.argv[2], 'r', (err, fd) => {
  fs.read(fd, buff, 0, 1024, 0, (err, bytes, buff) => {
    fs.open(process.argv[3], 'r', (err, fd2) => {
      fs.read(fd2, buff2, 0, 1024, 0, (err, bytes, buff2) => {
        fs.open(process.argv[4], 'a', (err, fd3) => {
          fs.write(fd3, buff, 0, 1024, 0, (err, bytes, buffer) => {
            fs.write(fd3, buff2, 0, 1024, 0, (err, bytes, buffer) => {

            });
          });
        });
      });
    });
	  });
	  });
