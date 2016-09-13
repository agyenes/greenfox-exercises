'use strict';

var conversion = require('./conversion');
var fs = require('fs');

fs.readFile('ARAB.IN.txt', 'utf8', function(err, data) {
  if (err) {
    throw 'File reading error';
  }
  var arabNumbers = data.split('\r\n');
  var romanNumbers = [];
  for (var i = 0; i < arabNumbers.length - 1; i++) {
    conversion.checkInput(arabNumbers[i]);
    romanNumbers.push(conversion.convertToRoman(arabNumbers[i]));
  }
  fs.writeFile('ROMAI.OUT.txt', romanNumbers.join('\r\n'));
});
