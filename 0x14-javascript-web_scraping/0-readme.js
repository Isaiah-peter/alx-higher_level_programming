#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const argv = process.argv;

fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
