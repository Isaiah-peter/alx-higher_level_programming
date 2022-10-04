#!/usr/bin/node

const process = require('process');

const argv = process.argv;

function factorial(n) {
  if (n == NaN) {
    console.log(1);
    return;
  }
  if (n == 1) {
    return 1
  }

  return n * factorial(n-1)
}

console.log(factorial(argv[2]))
