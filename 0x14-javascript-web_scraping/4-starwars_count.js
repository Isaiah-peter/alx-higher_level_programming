#!/usr/bin/node
// make a GET request and print the status code
const request = require('request');
let count = 0;
request(process.argv[2], function (error, response, body) {
  error && console.log(error);
  if (body) {
    const result = JSON.parse(body).results;

    for (const i of result) {
      if (i.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }

    console.log(count);
  }
});
