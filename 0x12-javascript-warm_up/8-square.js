#!/usr/bin/node
const size = process.argv[2];
let square = '';
if (isNaN(size) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    square += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(square);
  }
}
