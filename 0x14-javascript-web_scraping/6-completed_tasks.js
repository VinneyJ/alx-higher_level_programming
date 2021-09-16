#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const myDict = {};
  const bodyText = JSON.parse(body);
  const i = 0;

  while (i < bodyText.length) {
    const user = bodyText[i].userId;
    if (user in myDict) {
      myDict[user] += 1;
    } else {
      myDict[user] = 1;
    }
  }
  console.log(myDict);
});
