#!/usr/bin/node
const fs = require('fs');
const buff = Buffer.alloc(1024);
const buff2 = Buffer.alloc(1024);
fs.open(process.argv[2], 'r', (err, fd) => {
  if (err) { console.log(err); }
  fs.read(fd, buff, 0, 1024, 0, (err, bytes1, buff) => {
    if (err) { console.log(err); }
    fs.open(process.argv[3], 'r', (err, fd2) => {
      if (err) { console.log(err); }
      fs.read(fd2, buff2, 0, 1024, 0, (err, bytes2, buff2) => {
        if (err) { console.log(err); }
        fs.open(process.argv[4], 'a', (err, fd3) => {
          if (err) { console.log(err); }
          fs.write(fd3, buff, 0, bytes1, 0, (err, bytes, buffer) => {
            if (err) { console.log(err); }
            fs.write(fd3, buff2, 0, bytes2, 0, (err, bytes, buffer) => {
              if (err) { console.log(err); }
            });
          });
        });
      });
    });
  });
});
