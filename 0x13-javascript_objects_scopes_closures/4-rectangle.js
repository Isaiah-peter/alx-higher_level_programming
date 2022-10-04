#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let m = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        m += 'X';
      }

      if (i !== this.height - 1) {
        m += '\n';
      }
    }

    console.log(m);
  }
  double () {
    let m = '';
    for (let i = 0; i < this.height * 2; i++) {
      for (let j = 0; j < this.width * 2; j++) {
        m += 'X';
      }

      if (i !== this.height - 1) {
        m += '\n';
      }
    }

    console.log(m);
  }
  rotate () {
    let m = '';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        m += 'X';
      }

      if (i !== this.height - 1) {
        m += '\n';
      }
    }

    console.log(m);
  } 
}

module.exports = Rectangle;