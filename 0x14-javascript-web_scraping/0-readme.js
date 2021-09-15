#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  fs.readFile(argv[2], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
