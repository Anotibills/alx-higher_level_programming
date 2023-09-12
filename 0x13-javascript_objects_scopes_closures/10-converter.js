#!/usr/bin/node

exports.converter = function (base) {
  function convertToBase(num) {
    return num.toString(base);
  }

  return convertToBase;
};
