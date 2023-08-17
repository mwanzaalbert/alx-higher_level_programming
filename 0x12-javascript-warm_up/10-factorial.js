#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}

function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
