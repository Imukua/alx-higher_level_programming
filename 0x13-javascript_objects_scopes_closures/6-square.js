#!/usr/bin/node

class Square extends require('./5-square.js') {
  charPrint (c) {
    let printChar = c;
    if (c === undefined) {
      printChar = 'X';
    }

    for (let i = 0; i < this.size; i++) {
      console.log(printChar.repeat(this.size));
    }
  }
}

module.exports = Square;
