#!/usr/bin/node

const Square = require('./5-square.js');

class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let m = '';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        m += c;
      }
      if (i !== this.height - 1) {
        m += '\n';
      }
    }

    console.log(m);
  }
}

module.exports = Square;