#!/usr/bin/node

const argsPassed = Number.parseInt(process.argv[2]);

console.log(Number.isNaN(argsPassed) ? 'Not a number' : 'My number: ' + argsPassed);
