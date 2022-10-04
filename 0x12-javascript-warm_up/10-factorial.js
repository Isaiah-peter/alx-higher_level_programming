#!/usr/bin/node

const process = require('process');

const argv = process.argv;

function factorial (n) {
  if (n === 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

if (argv.length === 2) {
  console.log(1);
} else {
  console.log(factorial(argv[2]));
}
