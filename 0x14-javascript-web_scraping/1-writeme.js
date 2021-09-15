#!/usr/bin/node

const { argv } = require('process');

const fs = require('fs');


const content = argv[3];

fs.writeFile(argv[2], content, err => {
  if (err) {
    console.error(err)
    return
 }
   console.log('written succesfully');
})
