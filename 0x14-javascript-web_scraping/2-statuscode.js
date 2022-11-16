#!/usr/env/node

const process = require('process');
const request = require('request');

const argv = process.argv

request(argv[2], function (error, res, body) {
    console.log(res.statusCode)
})