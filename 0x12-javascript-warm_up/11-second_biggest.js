#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const myList = [];
  let i = 2;
  while (i < argv.length) {
    myList.push(argv[i]);
    i++;
  }
  const a = myList.sort();
  console.log(a[a.length - 2]);
}
