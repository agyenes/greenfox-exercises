'use strict';

var dog = function() {
  var sound = 'vvvvaaaaaaaaaaaa'
  return {
    talk: function() {
      console.log(sound);
    }
  }
}
var szurok = dog()
szurok.talk()
