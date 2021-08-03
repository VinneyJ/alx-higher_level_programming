#!/usr/bin/node

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
