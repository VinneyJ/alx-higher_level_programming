#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add (a, b) {
  if (a && b) {
    console.log(a + b);
  } else {
    console.log('NaN');
  }
}
add(a, b);
