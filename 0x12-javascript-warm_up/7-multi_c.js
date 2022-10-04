#!/usr/bin/node

const process = require('process');

const argv = process.argv;

if (argv[2] !== undefined) {
  for(let i = 0; i < argv[3]; i++) {
    console.log('C is fun');
  }
} else if (Number(argv[2] === NaN)) {
  console.log('Missing number of occurrences');
} else {
  return;
}