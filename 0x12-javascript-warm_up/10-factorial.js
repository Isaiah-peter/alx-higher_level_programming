#!/usr/bin/node

const process = require('process');

const argv = process.argv;

let num = 1;

if (argv[2] !== undefined) {
  for (let i = 1; i <= Number(argv[2]); i++) {
    num *= i;
  }

  console.log(num);
} else {
  console.log(1);
}
