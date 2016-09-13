'use strict';

var dog = function() {
  var sound = 'vvvvaaaaaaaaaaaa'

  function publicTalk () {
    console.log(sound);
  }

  return {
    talk: publicTalk
  }
}();

dog.talk()
