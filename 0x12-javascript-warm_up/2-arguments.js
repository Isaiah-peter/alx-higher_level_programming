#!/usr/bin/node

const process = require('process');

const argv = process.argv;

if (argv.length === 3) {
  console.log('Argument found');
} else if (argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
