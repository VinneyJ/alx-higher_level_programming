#!/usr/bin/node
const { argv } = require('process');

let i = 0;
if (argv.length === 2) {
  console.log('Missing number of occurences');
} else {
  while (i < parseInt(argv[2])) {
    console.log('C is fun');
    i++;
  }
}
