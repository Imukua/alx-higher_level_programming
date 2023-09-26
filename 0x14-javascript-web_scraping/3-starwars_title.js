#!/usr/bin/node
const request = require('request');
// set url
const urls = 'http://swapi.co/api/films/' + process.argv[2];
request(urls, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
