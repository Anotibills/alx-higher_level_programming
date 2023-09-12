#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = Object.entries(dict).reduce((acc, [userId, numOccurrences]) => {
  if (!acc[numOccurrences]) {
    acc[numOccurrences] = [];
  }
  acc[numOccurrences].push(userId);
  return acc;
}, {});

console.log(newDict);
