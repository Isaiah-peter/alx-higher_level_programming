#!/usr/bin/node

const process = require('process');

const argv = process.argv;

let str = '';

for (let i = 0; i < Number(argv[2]); i++) {
  for (let j = 0; j < Number(argv[2]); j++) {
    str += 'X';
  }

  if (i !== Number(argv[2]) - 1){
    str += '\n';
  }
}

console.log(str);
