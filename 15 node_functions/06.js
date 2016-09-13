'use strict';

// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function isLetterInString(input_string, letter) {
  if (input_string.indexOf(letter) === -1) {
    return false
  } else {
    return true
  }
};

console.log(isLetterInString('apple', 'a'));
console.log(isLetterInString('apple', 'f'));
