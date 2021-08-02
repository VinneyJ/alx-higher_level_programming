#!/usr/bin/node

const { argv } = require('process');

function arrayLen (a) {
  let length = 0;
  while (a[length] !== undefined) {
    length++;
  }
  return length;
}

// print process.argv
if (arrayLen(argv) <= 2) {
  console.log('No argument');
} else if (arrayLen(argv) === 3 || arrayLen(argv) > 2) {
  argv.slice(2).forEach((val) => {
    console.log(val);
  });
}
