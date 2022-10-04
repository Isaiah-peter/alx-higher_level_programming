#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let result = 0;

  for(let i in list) {
    if (i == searchElement) {
      result += 1;
    }
  }

  return result;
}