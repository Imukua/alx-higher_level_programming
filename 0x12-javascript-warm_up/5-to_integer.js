#!/usr/bin/node

const firstArg = process.argv[2];
const intArg = parseInt(firstArg);

if (!isNaN(intArg)) {
  console.log(`My number: ${intArg}`);
} else {
  console.log('Not a number');
}
