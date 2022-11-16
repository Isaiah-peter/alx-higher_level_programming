#!/usr/bin/node
// make a GET request and print the status code
const request = require('request');
const count = {};
request(process.argv[2], function (error, response, body) {
  error && console.log(error);
  if (body) {
    const result = JSON.parse(body);
    result.forEach((i) => {
      if (count[i.userId]) {
        if (i.completed == true) {
          count[i.userId] = count[i.userId] + 1;
        }
      } else {
        if (i.completed == true) {
          count[i.userId] = 1;
        }
      }
    });

    console.log(count);
  }
});
