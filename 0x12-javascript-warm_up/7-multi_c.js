#!/usr/bin/node
const argv = process.argv[2];
if (isNaN(argv) === true) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < argv; i++) {
  console.log('C is fun');
}
