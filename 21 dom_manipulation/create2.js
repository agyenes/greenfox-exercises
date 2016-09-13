'use strict';

var asteroidList = document.querySelector('ul');
var king = document.querySelector('li');
asteroidList.removeChild(king);

for (var i = 0; i < 3; i++) {
  var newListElement = document.createElement('li');
  newListElement.textContent = 'The Fox';
  asteroidList.appendChild(newListElement);
}
