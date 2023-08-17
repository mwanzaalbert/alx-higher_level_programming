#!/usr/bin/node
let numOfArguments = 0;
exports.logMe = function (item) {
  console.log(numOfArguments + ': ' + item);
  numOfArguments += 1;
};
