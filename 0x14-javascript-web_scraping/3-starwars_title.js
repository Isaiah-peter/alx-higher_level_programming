#!/usr/bin/node
// make a GET request and print the status code
const request = require('request');
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  error && console.log(error);
  body && console.log(JSON.parse(body).title);
});
