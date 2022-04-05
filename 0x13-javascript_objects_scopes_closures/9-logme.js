#!/usr/bin/node
var xxx = 0;
exports.logMe = function (item) {
  console.log(xxx + ' ' + item);
  xxx++;
};
