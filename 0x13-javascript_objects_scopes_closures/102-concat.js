#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
	console.error('Usage: node 102-concat.js <fileA> <fileB> <fileC>');
	process.exit(1);
}

const fileAPath = args[0];
const fileBPath = args[1];
const fileCPath = args[2];

const contentA = fs.readFileSync(fileAPath, 'utf8');
const contentB = fs.readFileSync(fileBPath, 'utf8');
const concatenatedContent = contentA + contentB;

fs.writeFileSync(fileCPath, concatenatedContent);
