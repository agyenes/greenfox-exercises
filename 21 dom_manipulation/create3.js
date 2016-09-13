'use strict';

var asteroidList = document.querySelector('ul');
var king = document.querySelector('li');
asteroidList.removeChild(king);

var new_list = ['apple', 'bubble', 'cat', 'green fox']

for (var i = 0; i < new_list.length; i++) {
  var newListElement = document.createElement('li');
  newListElement.textContent = new_list[i];
  asteroidList.appendChild(newListElement);
}
