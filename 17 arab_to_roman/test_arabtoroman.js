'use strict';

var tape = require('tape');
var conversion = require('./conversion');

tape('singleDigitNumber', function(t) {
  t.deepEqual(conversion.convertToRoman(1), 'I');
  t.end();
});

tape('numberWithSubtraction', function(t) {
  t.deepEqual(conversion.convertToRoman(9), 'IX');
  t.end();
});

tape('doubleDigitNumber', function(t) {
  t.deepEqual(conversion.convertToRoman(56), 'LVI');
  t.end();
});

tape('doubleDigitNumberWithSubtraction', function(t) {
  t.deepEqual(conversion.convertToRoman(89), 'LXXXIX');
  t.end();
});

tape('doubleDigitNumberWithTwoSubtractions', function(t) {
  t.deepEqual(conversion.convertToRoman(99), 'XCIX');
  t.end();
});

tape('tripleDigitNumber', function(t) {
  t.deepEqual(conversion.convertToRoman(738), 'DCCXXXVIII');
  t.end();
});

tape('tripleDigitNumberWithSubtractions', function(t) {
  t.deepEqual(conversion.convertToRoman(499), 'CDXCIX');
  t.end();
});

tape('fourDigitNumber', function(t) {
  t.deepEqual(conversion.convertToRoman(3237), 'MMMCCXXXVII');
  t.end();
});

tape('fourDigitNumberWithSubtractions', function(t) {
  t.deepEqual(conversion.convertToRoman(1999), 'MCMXCIX');
  t.end();
});
