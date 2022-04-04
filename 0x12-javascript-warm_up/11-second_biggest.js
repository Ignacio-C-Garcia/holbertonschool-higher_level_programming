#!/usr/bin/node
if (process.argv[2] === undefined) { console.log('0'); } else {
  let array = process.argv.slice(2);
  array = array.map(element => parseInt(element));
  const unicos = [...new Set(array)];
  array = Array.from(unicos);
  array.sort(function (a, b) {
    return a - b;
  });
  if (array.length === 1) { console.log(0); } else {
    console.log(array[array.length - 2
    ]);
  }
}
