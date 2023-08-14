#!/usr/bin/node

const numTimes = process.argv[2];
let intValue = parseInt(numTimes);
const charPrint = 'C is fun';
if (!isNaN(intValue)) {
  while (intValue > 0) {
    console.log(charPrint);
    intValue--;
  }
} else {
  console.log('Missing number of occurences');
}
