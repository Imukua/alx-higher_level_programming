#!/usr/bin/node
// load the filesystem module
const fs = require('fs');
// open the file, print error incase any
fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
