'use strict';

var newAsteroid = document.createElement('li');
var newAsteroid2 = document.createElement('li');
var asteroidList = document.querySelector('ul');

newAsteroid.textContent = 'The Green Fox';
asteroidList.appendChild(newAsteroid);
newAsteroid2.textContent = 'The Lamplighter';
asteroidList.appendChild(newAsteroid2);

var newHeader = document.createElement('h1');
var container = document.querySelector('.container');
newHeader.textContent = 'I can add elements to the DOM!';
container.appendChild(newHeader);

var newImage = document.createElement('img');
newImage.setAttribute('src', 'http://www.popoptiq.com/wp-content/uploads/2014/05/Nosferatu-3.jpg')
container.appendChild(newImage);
