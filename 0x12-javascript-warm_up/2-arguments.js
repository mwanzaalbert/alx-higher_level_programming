#!/usr/bin/node
const argsPassed = process.argv.length;

if (argsPassed > 2) {
  console.log('Argument' + (argsPassed > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
