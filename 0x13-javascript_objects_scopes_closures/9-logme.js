#!/usr/bin/node
xxx = 0;
exports.logMe = function (item) {
  console.log(xxx + ': ' + item);
  xxx++;
};
