#!/usr/bin/node

const oldList = require('./100-data').list;
newList = oldList.map((num, idx) => num * idx);

console.log(oldList);
console.log(newList);
