#!/usr/bin/node
let xxx = 0;
exports.logMe = function (item) {
  console.log(xxx + ': ' + item);
  xxx++;
};
