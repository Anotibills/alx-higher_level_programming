#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  } else {
    console.error(error);
  }
});

function printCharacters (characters, idx) {
  if (idx >= characters.length) {
    return;
  }

  request(characters[idx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
    } else {
      console.error(error);
    }

    printCharacters(characters, idx + 1);
  });
}
