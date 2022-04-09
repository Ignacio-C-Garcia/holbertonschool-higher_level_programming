#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const _width = this.width;
    let _height = this.height;
    while (_height) {
      console.log('X'.repeat(_width));
      _height--;
    }
  }
};
