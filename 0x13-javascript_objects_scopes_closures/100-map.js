#!/usr/bin/node

const list = require('./100-data.js').list;

console.log(list)
let arr = list.map((x, i)=> x * i)
console.log(arr)