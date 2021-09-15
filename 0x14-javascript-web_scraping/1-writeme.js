#!/usr/bin/node

const { argv } = require('process');

const fs = require('fs');

const content = argv[3];

try {
  fs.writeFileSync(argv[2], content);
  // file written successfully
  console.log('written succesfully');
} catch (err) {
  console.error(err);
}
