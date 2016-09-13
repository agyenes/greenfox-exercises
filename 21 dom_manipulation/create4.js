'use strict';

var asteroidList = document.querySelector('.asteroids');
var king = document.querySelector('li');
asteroidList.removeChild(king);

var new_list = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]

new_list.forEach(function(e) {
  var newLi = document.createElement('li');
  if (e.asteroid) {
    newLi.textContent = e.content;
    newLi.classList.add(e.category);
    asteroidList.appendChild(newLi);
  }
});
