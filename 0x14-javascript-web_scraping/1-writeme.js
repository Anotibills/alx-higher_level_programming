#!/usr/bin/node

const fs = require('fs');

async function writeFileAsync () {
  try {
    await fs.promises.writeFile(process.argv[2], process.argv[3]);
  } catch (err) {
    console.error(err);
  }
}

writeFileAsync();
