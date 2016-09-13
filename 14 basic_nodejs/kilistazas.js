// Create a function that counts the cars by colors
// With an output like: {red: 3, yellow: 2, white: 1, green: 1}

'use strict';

const cars = [{
    color: 'red',
    type: 'Volvo'
  }, {
    color: 'yellow',
    type: 'VW'
  }, {
    color: 'red',
    type: 'Ferrari'
  }, {
    color: 'white',
    type: 'Tesla'
  }, {
    color: 'yellow',
    type: 'Toyota'
  }, {
    color: 'red',
    type: 'Lada'
  }, {
    color: 'green',
    type: 'Trabant'
}];

function counter(input) {
  var outputObject = {};
  input.forEach(function(e) {
    if (!(e.color in outputObject)) {
      outputObject[e.color] = 1;
    } else {
      outputObject[e.color] += 1;
    }
  })
  return outputObject;
}

console.log(counter(cars));
