#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body).results;
    for (let i = 0; i < data.length; i++) {
      const characters = data[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.error(error);
  }
});
