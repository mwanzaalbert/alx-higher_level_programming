#!/usr/bin/node

const x = Number.parseInt(process.argv[2]);
const y = Number.parseInt(process.argv[3]);

const sum = add(x, y);

function add (a, b) {
  if (Number.isNan(a) || Number.isNan(b)) {
    return 'NaN';
  } else {
    return (a + b);
  }
}

console.log(sum);
