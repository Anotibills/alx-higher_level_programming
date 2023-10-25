#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const outputFile = process.argv[3];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(outputFile, body, 'utf-8', function (err) {
      if (!err) {
        console.log('File saved successfully: ' + outputFile);
      } else {
        console.error('Error saving the file: ' + err);
      }
    });
  } else {
    console.error(error);
  }
});
