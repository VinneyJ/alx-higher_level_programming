#!/usr/bin/node

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
