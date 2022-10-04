#!/usr/bin/node

const process = require('process');

const argv = process.argv;

let num = 1

if (argv[2] !== undefined) {
  for(let i = 0; i < argv[2]; i++) {
    number *= i
  }
  
  console.log(num)
} else {
  console.log(1)
}
