#!/usr/bin/node

import { list } from './100-data.js';
newList = list.map((num, idx) => num * idx);

console.log(list);
console.log(newList);
