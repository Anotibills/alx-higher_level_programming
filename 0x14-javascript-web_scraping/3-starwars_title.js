#!/usr/bin/node

const request = require('request');

const url = 'http://swapi.dev/api/films/';

request(url + process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    console.log(filmData.title);
  } else {
    console.error(error);
  }
});
