'use strict';

var all_paragraphs = document.querySelectorAll('p');
var last_paragraph = document.querySelector('.dog');

for (var i = 0; i < all_paragraphs.length; i++) {
  all_paragraphs[i].textContent = last_paragraph.textContent;
};
