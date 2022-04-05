#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) { super(size, size); }
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    if (this.height === undefined || this.width === undefined) { return; }
    let height = this.height;
    while (height) {
      console.log(c.repeat(this.width));
      height--;
    }
  }
};
