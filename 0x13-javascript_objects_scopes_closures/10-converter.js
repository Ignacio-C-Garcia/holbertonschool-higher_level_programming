#!/usr/bin/node
exports.converter = function (base) {
  function parse (x) {
    return x.toString(base);
  }
  return parse;
};
