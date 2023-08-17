#!/usr/bin/node

const data = require('./101-data'); // Import the dictionary from 101-data.js

const initialDict = data.dict;
const userOccurrences = {};

for (const userId in initialDict) {
	  const occurrences = initialDict[userId];
	  if (!userOccurrences[occurrences]) {
		      userOccurrences[occurrences] = [];
		    }
	  userOccurrences[occurrences].push(userId);
}

console.log(userOccurrences);
