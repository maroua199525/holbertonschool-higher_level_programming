#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let ch = '';
    for (let j = 0; j < this.width; j++) {
      ch += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(ch);
    }
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
