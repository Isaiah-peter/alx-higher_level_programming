#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let result = 0;

  for (const i of list) {
    if (i === searchElement) {
      result += 1;
    }
  }

  return result;
};
