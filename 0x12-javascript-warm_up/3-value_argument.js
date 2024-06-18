#!/usr/bin/node

const argsPassed = process.argv[2];

console.log(argsPassed !== undefined ? argsPassed : 'No argument');
