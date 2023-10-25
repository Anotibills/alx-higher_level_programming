#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi.dev/api/films/';

request(url + id, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error(error);
        }
      });
    });
  } else {
    console.error(error);
  }
});
