#!/usr/bin/node
//load the module
const fs = require("fs");
// read the file
fs.readFile(process.argv[2], "utf8", function (error, content) {
  console.log(error || content);
});
