#!/usr/bin/node

let i = 0;
if (process.argv.length === 2) {
  console.log('Missing number of occurences');
} else {
  while (i < parseInt(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
}
