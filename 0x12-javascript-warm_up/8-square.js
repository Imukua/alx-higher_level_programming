#!/usr/bin/node

const Size = process.argv[2];
const intValue = parseInt(Size);
const charPrint = 'X';
if (!isNaN(intValue)) {
  for (let i = 0; i < intValue; i++) {
    console.log(charPrint.repeat(Size));
  }
} else {
  console.log('Missing size');
}
