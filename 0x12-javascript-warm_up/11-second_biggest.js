#!/usr/bin/node
if (process.argv.length <= 3) {
	console.log('0');
} else {
  const arrays = process.argv.slice(2).map(Number);
  const secBig = arrays.sort(function (x, y) { return y - x; })[1];
  console.log(secBig);
}
