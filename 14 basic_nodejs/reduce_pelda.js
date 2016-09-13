'use strict';

var numbers = [4, 5, 2, 15, 9];

var sum = numbers.reduce(function(acc, e, i, arr) {
  return acc += e
});
