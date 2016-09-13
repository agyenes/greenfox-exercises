'use strict';

var cat = document.querySelector('.cat');
var all_paragraphs = document.querySelectorAll('p');
var dolphin = all_paragraphs[3]
var apple = document.querySelector('p');
var balloon = all_paragraphs[1];

if (dolphin.classList.value === 'dolphin') {
  apple.textContent = 'pear';
}

if (apple.classList.value === 'apple') {
  cat.textContent = 'dog';
}

apple.setAttribute('style', 'color: red');

balloon.setAttribute('style', 'border-radius: 10%');


//
//
