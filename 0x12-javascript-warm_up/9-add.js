#!/usr/bin/node

const process = require('process');

const argv = process.argv;

if (argv[2] == undefined || argv[3] == undefined) {
  console.log(NaN);
} else {
  console.log(argv[2] + argv[3])
}