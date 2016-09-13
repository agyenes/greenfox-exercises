'use strict';

var header = document.querySelector('h1');
alert(header.innerHTML);

var first_para = document.querySelector('p');
console.log(first_para.innerHTML);

var second_para = document.querySelector('.other');
alert(second_para.innerHTML);

var header = document.querySelector('h1');
header.textContent = 'New content';

var last_para = document.querySelector('.result');
last_para.textContent = first_para.textContent
