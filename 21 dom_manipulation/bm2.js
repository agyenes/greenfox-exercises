'use strict';

var headers = document.querySelectorAll('h1');

headers.forEach(function (e) {
  e.textContent = 'Green Fox Academy Conquers the World'
});


'use strict';
// Create a script that replaces every image
// with this: http://bit.ly/lpgreenfox
// Create a bookmarklet that does that on any website.

var photos = document.querySelectorAll('img');

photos.forEach(function (e) {
  e.setAttribute('src', 'http://bit.ly/lpgreenfox');
});
