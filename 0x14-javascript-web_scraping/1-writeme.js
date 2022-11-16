#!/usr/bin/node

const process = require('process');
const fs = require('fs');


const argv = process.argv;
const text = argv[3]

fs.writeFile(argv[2], text, (err) => {
    if (err != null) {
        console.log("file write error");
    }
});