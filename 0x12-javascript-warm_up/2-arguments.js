#!/usr/bin/node
const arg_passed = process.argv.length;

if (arg_passed > 2) {
	console.log('Argument' + (argc > 3 ? 's' : '') + ' found');
} else {
	console.log('No argument');
}
