'use strict';

var image_url = document.querySelector('img');
console.log(image_url.getAttribute('src'));

image_url.setAttribute('src', 'http://www.vampyres-online.com/images/klaus_kinski_big.jpg');

var anchor = document.querySelector('a');
anchor.setAttribute('href', 'http://www.greenfoxacademy.com/');

var second_button = document.querySelector('.this-one');
second_button.disabled = true;

second_button.textContent = 'Don\'t click me!'
