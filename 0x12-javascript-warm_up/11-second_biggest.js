#!/usr/bin/node

const process = require('process');

const argv = process.argv;

let lagest = argv[2]
let sec = argv[3]

for(let i of argv) {
  if (i > lagest) {
    lagest = i
  }
}

for(let i of argv) {
  if (i > sec && sec < lagest) {
    sec = i
  }
}

return sec