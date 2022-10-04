#!/bin/node

const process = require('process');
const argv = process.argv;

if (Number(argv[2]) === NaN) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(argv[2]));
}