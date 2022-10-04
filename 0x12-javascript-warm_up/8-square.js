#!/usr/bin/node

const process = require('process');

const argv = process.argv;

let str = '';

for (let i = 0; i < argv[2]; i++) {
  for (let j = 0; j < argv[2]; j++) {
    str += 'X';
  }

  str += '\n';
}

console.log(str);
