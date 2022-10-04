#!/usr/bin/node

const process = require('process');

const argv = process.argv;

let lagest = Number(argv[2]);
let sec = 0;

for (const i of argv) {
  if (Number(i) > lagest) {
    lagest = Number(i);
  }
}

for (const i of argv) {
  if (Number(i) > sec && i < lagest) {
    sec = Number(i);
  }
}

if (argv.length < 4) {
  sec = 0;
}

console.log(sec);
