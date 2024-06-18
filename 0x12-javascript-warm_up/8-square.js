#!/usr/bin/node
const charToPrint = 'X';
const squareSize = Number.parseInt(process.argv[2]);

if (Number.isNaN(squareSize)) {
  console.log('Missing size');
} else if (squareSize >= 2) {
  for (let row = 0; row < squareSize; row++) {
    for (let column = 0; column < squareSize; column++) {
      process.stdout.write(charToPrint);
    }
    console.log();
  }
}
