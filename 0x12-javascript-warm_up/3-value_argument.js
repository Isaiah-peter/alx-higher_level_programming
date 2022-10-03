#!/usr/bin/node

import { argv } from 'node:process';

if (argv[3] != undefined) {
  console.log(argv[3]);
} else {
  console.log('No argument');
}