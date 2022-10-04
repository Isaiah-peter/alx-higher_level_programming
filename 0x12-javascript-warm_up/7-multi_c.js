#!/usr/bin/node

const process = require('process');

const argv = process.argv;

if (argv[2] !== undefined) {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
} else if (argv[2] === undefined || argv[2] >= 0) {
  console.log('Missing number of occurrences');
}
