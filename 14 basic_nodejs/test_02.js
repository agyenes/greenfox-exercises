'use strict';

var test = require('tape');
var myFunction = require('./02');
var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

var students2 = [
  {name: 'Steve', age: 12, books: []},
  {name: 'Ryan', age: 11, books: []},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: []},
];

var students3 = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: ['Grapes of Wrath']},
  {name: 'Steve', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

test('test basic', function (t) {
    t.deepEqual(myFunction(students), 4);
    t.end();
});

test('test empty', function (t) {
    t.deepEqual(myFunction(students2), 0);
    t.end();
});

test('test repeating names', function (t) {
    t.deepEqual(myFunction(students3), 5);
    t.end();
});
