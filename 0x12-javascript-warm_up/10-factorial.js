#!/usr/bin/node

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const intvalue = parseInt(process.argv[2]);

console.log(factorial(intvalue));
