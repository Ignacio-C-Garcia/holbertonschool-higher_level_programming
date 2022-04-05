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
    if (_width === undefined) { return; }
    while (_height) {
      console.log('X'.repeat(_width));
      _height--;
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    if (this.width !== undefined) { this.width *= 2; }
    if (this.height !== undefined) { this.height *= 2; }
  }
};
