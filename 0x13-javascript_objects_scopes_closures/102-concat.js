#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

try {
  const content1 = fs.readFileSync(sourceFile1, 'utf8');
  const content2 = fs.readFileSync(sourceFile2, 'utf8');
  const concatenatedContent = content1 + content2;

  fs.writeFileSync(destinationFile, concatenatedContent, 'utf8');
  console.log(`Concatenated ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
} catch (error) {
  console.error('An error occurred:', error.message);
}
