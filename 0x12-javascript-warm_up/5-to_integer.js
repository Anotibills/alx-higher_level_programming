#!/usr/bin/node
const argTwo = process.argv[2];
const parsedNum = parseInt(argTwo);
if (isNaN(parsedNum)) {
	console.log('Not a umber');
}
else {
	console.log('My Number: $(parsedNum)');
}
