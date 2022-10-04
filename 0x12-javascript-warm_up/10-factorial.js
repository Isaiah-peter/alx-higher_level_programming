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
  } else if (n == 2) {
    return 2
  }

  return factorial(n-1) * factorial(n-2)
}

console.log(factorial(argv[2]))
