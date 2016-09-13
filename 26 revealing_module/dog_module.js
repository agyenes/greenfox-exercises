'use strict';

var dog = ( function() {
  var sound = 'vvvvaaaaaaaaaaaa'
  return {
    talk: function() {
      console.log(sound);
    }
  }
})();

dog.talk()
