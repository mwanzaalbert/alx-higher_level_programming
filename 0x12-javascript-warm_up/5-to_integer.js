#!/usr/bin/node
let numToConvert = process.argv[2];
numToConvert = parseInt(numToConvert);
if (isNaN(numToConvert)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numToConvert);
}
