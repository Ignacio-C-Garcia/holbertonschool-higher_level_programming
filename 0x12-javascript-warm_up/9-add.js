#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return a + b;
}
console.log(add(a, b));
