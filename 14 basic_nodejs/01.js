'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function letter_count(input_string) {
  var letters = {};
  String(input_string).split('').forEach(function(e) {
    letters[e] = (letters[e] || 0) + 1;
  });
  return letters;
}

module.exports = letter_count
