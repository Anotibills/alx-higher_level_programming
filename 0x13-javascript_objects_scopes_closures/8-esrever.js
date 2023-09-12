#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  let a = 0;

  while (len > a) {
    const temp = list[len];
    list[len] = list[a];
    list[a] = temp;
    a++;
    len--;
  }

  return list;
};
