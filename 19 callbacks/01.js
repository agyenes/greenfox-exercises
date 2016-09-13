'use strict';

// create a function that takes a filename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count

var fs = require('fs');

function wordCounter(filename, cb) {
  fs.readFile(filename, function(err, content) {
    if (err) {
      return cb(err);
    }
    var counter = (String(content).split(/\s/g)).length;
    cb(err, counter);
    });
  };

function writeOut(err, counter){
  console.log(err, counter);
}

wordCounter('majom.txt', writeOut)

//
// wordCount ('alma.txt', function(err, c) {
//   console.log(err, c)
// }
//
// function wordCount (filename, cb) {
//   cb(null, 5);
// }
