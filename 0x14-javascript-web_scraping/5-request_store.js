#!/usr/bin/node
const fs = require('fs');
// load request module
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]))
