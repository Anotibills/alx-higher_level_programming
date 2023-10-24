#!/usr/bin/node

const fs = require('fs');

fs.promises.readFile(process.argv[2], 'utf-8')
  .then(data => {
    console.log(data);
  })
  .catch(err => {
    console.log(err);
  });
