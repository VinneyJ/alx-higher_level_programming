#!/usr/bin/node

const { argv } = require('process');

/*
let num = parseInt(process.argv[2]);
function fact (a) {
  if (a === '0' || isNaN(a)) {
    return (1);
  } else {
    let i = 1;
    while (num >= 1) {
      i *= num;
      num--;
    }
    return (i);
  }
}

console.log(fact(num));
*/

const argInt = parseInt(argv[2]);
function fact (arg) {
  if (arg) {
    if (arg === 1) {
      return 1;
    } else {
      return arg * fact(arg - 1);
    }
  }
}
function check () {
  if (argv.length === 3) {
    const result = fact(argInt);
    console.log(`${result}`);
  } else {
    console.log(1);
  }
}

check();
