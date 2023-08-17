#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
// process.argv get the arguments and parseInt() convert str to int
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
