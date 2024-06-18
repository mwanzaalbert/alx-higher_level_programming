#!/usr/bin/node

const argsData = process.argv.slice(2).map(Number);

const secondLargest = getSecondLargest(argsData);

function getSecondLargest (argList) {
  if (argList.length < 2) {
    return 0;
  } else {
    const sortedData = [...(argList)].sort((a, b) => b - a);
    return sortedData[sortedData.length - 2];
  }
}

console.log(secondLargest);
