'use strict';

var numbers = [2, 5, 11, 29, 19];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function areNumbersPrime(arr) {
  for (var j = 0; j < arr.length; j++) {
    for (var i = 2;i < arr[j]; i++) {
      if (arr[j] % i === 0) {
        return false;
        break
      }
    } return true
  }
}

console.log(areNumbersPrime(numbers));
