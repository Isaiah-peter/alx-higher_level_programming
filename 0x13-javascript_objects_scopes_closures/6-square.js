#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle {
  constructor (size) {
    super(size, size)
  }

  charPrint(c='X') {
    let m = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        m += c;
      }

      if (i !== this.height - 1) {
        m += '\n';
      }
    }

    console.log(m);
  }
}

module.exports = Square