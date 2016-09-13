'use strict';

var fs = require('fs');

fs.readFile('majom.txt', function(err, c) {
  console.log(String(c));
  fs.writefile('korte.txt', String(c) + 'beka'), function(err, c) {
    console.log('end');
  });
});

console.log('for elott')


for (var i; i < 1000; i++) {
  i + 3;
}

console.log('vmi');
