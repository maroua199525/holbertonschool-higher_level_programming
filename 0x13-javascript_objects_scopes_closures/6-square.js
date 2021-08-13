#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Now 'this' is initialized by calling the parent constructor.
  }

  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let ch = '';
      for (let j = 0; j < this.width; j++) {
        ch += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(ch);
      }
    }
  }
};
