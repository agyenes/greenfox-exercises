'use strict';
// Turn the party on and off by clicking the button.

var list_items = document.querySelectorAll('li');
var result = document.querySelector('.result');

function countListItems() {
  var counter = list_items.length;
  result.textContent = counter
};

var button = document.querySelector('button');
button.addEventListener('click', countListItems);
