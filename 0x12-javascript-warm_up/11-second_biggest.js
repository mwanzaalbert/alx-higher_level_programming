#!/usr/bin/node
const arg = process.argv;
const size = arg.length;
// process.argv occupies the first two positions of the array
// The first element is the process execution path
// the second element is the path for the js file.
if (size <= 3) {
  console.log(0);
} else {
  arg.sort(function (a, b) {
    return a - b;
  });
  const secondBiggest = arg[size - 2];
  console.log(secondBiggest);
}
