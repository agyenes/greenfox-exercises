'use strict';

// create a function called apply that takes a function and calls it with one argument
// that is the string 'apple'

function apply(func, arg) {
  func(arg);
}

function write(arg) {
  console.log('Hi ' + arg + '!');
}

apply(write, 'apple')
