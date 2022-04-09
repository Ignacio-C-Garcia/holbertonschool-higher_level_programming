#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) { console.log('Missing size'); }
let size2 = size;
while (size2) {
  console.log('X'.repeat(size));
  size2--;
}
