#!/usr/bin/node

const x = Number.parseInt(process.argv[2]);
const y = Number.parseInt(process.argv[3]);

function add (a, b) {
  if (Number.isNaN(a) || Number.isNaN(b)) {
    return 'NaN';
  } else {
    return (a + b);
  }
}

let sum = add(x, y);
console.log(sum);
