#!/usr/bin/node

const process = require('process');

const argv = process.argv;

if (argv[2] === undefined || argv[3] === undefined) {
  console.log(NaN);
} else {
  console.log(Number(argv[2]) + Number(argv[3]));
}
