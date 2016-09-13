'use strict';

var dog = function() {
  this.sound = 'vvvvaaaaaaaaaaaa';
};

dog.prototype.talk = function () {
  console.log(this.sound);
};

var zsele = new dog;
zsele.talk();
