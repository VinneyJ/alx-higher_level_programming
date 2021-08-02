#!/usr/bin/node

const { argv } = require('process');
/*
//Find out the len of the array
function arrayLen (a) {
  let length = 0;
  while (a[length] !== undefined) {
    length++;
  }
  return length;
}
*/
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
/*
//print 1 or more arguments
// print process.argv
if (arrayLen(argv) <= 2) {
  console.log('No argument');
} else if (arrayLen(argv) === 3 || arrayLen(argv) > 2) {
  argv.slice(2).forEach((val) => {
    console.log(val);
  });
}
*/
