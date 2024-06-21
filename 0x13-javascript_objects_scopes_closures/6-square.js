#!/usr/bin/node
const SquareParent = require('./5-square');

/**
 * Represents a Rectangle with 4 equal sides.
 */
class Square extends SquareParent {
  /**
   * Prints this Square with the given character, otherwise 'X'.
   * @param {String} c The character to print this Square with.
   */
  charPrint (toPrint = '') {
    if (toPrint) {
      for (let counter = 0, row = this.height; counter < row; counter++) {
        for (let count = 0, col = this.width; count < col; count++) {
          process.stdout.write(toPrint);
        }
        console.log();
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
