#!/usr/bin/node
// Load request module
const request = require('request');
// get request
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
