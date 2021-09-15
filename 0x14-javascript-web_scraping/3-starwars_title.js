#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const id = parseInt(argv[2]);
const content = 'https://swapi-api.hbtn.io/api/films/';

const actual = content + id;
request(actual, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
