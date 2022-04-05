#!/usr/bin/node
exports.callMeMoby = function (x, fun) {
  while (x > 0) {
    fun();
    x--;
  }
};
