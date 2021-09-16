#!/usr/bin/node

const request = require('request');
const url = process.argv[2];


request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let x = 0;
    let count = 0;
    while (x < results.length) {
      const dicts = results[x];
      const characters = dicts.characters;
      x++;
      let y = 0;
      while (y < characters.length) {
        if (characters[y].match(/18/)) {
          count += 1;
        }
        y++;
      }
    }
    console.log(count);
  }
});
