'use strict';

var list_items = document.querySelectorAll('li');
console.log(list_items)

var new_list = ['apple', 'banana', 'cat', 'dog']

for (var i = 0; i < list_items.length; i++) {
  list_items[i].textContent = new_list[i];
}

//list_items.forEach(function (e,i) {e.innerHTML = new_list[i];})
