#!/usr/bin/node

const { argv } = require('process');
/*
//Option 1
const arg = parseInt(process.argv[2]);
let inLine = '';
let num = 0;
if (process.argv.length === 3 && arg) {
  while (num < arg) {
    inLine += 'X';
    num++;
  }
  let numnum = 0;
  while (numnum < arg) {
    console.log(inLine);
    numnum++;
  }
} else {
  console.log('Missing size');
}
*/

/*
  Option 2
*/
const arg = parseInt(argv[2]);
let string = '';
let counter = 0;

if (argv.length === 3 && arg) {
  while (counter < arg) {
    string += 'x';
    counter++;
  }
  let secondCounter = 0;
  while (secondCounter < counter) {
    console.log(string);
    secondCounter++;
  }
} else {
  console.log('Missing size');
}
