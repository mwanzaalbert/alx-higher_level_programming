#!/usr/bin/node
/**
 * Represents a parallelogram with 4 right angles.
 */
class Rectangle {
  /**
   * Creates a new Rectangle with the given dimensions.
   * @param {Number} w The value of the width.
   * @param {Number} h The value of the height.
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * Prints this Rectangle with the character 'X'.
   */
  print () {
    for (let counter = 0, row = this.height; counter < row; counter++) {
      for (let count = 0, col = this.width; count < col; count++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}

module.exports = Rectangle;
