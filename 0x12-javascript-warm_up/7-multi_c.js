#!/usr/bin/node
let repeat = parseInt(process.argv[2]);
if (isNaN(repeat)) { console.log('Missing number of occurrences'); }
while (repeat) {
  console.log('C is fun');
  repeat--;
}
