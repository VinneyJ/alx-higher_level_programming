#!/usr/bin/node
const { argv } = require('process');

/*
//OPTION 1

const arg1 = parseInt(argv[2]);
const arg2 = parseInt(argv[3]);
function add (a, b) {
  if (arg1 && arg2) {
    console.log(arg1 + arg2);
  } else {
    console.log('NaN');
  }
}
add(a, b);
*/

/*
  OPTION 2
*/

function add () {
  if (argv.length === 4) {
    const arg1 = parseInt(argv[2]);
    const arg2 = parseInt(argv[3]);
    let result = 0;
    if (arg1 && arg2) {
      argv.forEach((item) => {
        result = (arg1 + arg2);
      });
      console.log(result);
    }
  } else {
    console.log('NaN');
  }
}

add();
