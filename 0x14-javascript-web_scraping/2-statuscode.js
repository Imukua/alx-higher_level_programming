#!/usr/bin/node
const request = require('request');
//send get request
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
