#!/usr/bin/node
let number = parseInt(process.argv[2]);
if (isNaN(number)) { number = 1; }
function factorial (number) {
  let result = 0;
  if (number === 0) { return 1; }
  result = number * factorial(number - 1);
  return result;
}
console.log(factorial(number));
