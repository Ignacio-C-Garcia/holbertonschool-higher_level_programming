#!/usr/bin/node
exports.callMeMoby = function (x, fun) {
  while (x) {
    fun();
    x--;
  }
};
