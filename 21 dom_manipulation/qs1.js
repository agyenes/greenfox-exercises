'use strict';

var king = document.querySelector('#b325');
console.log(king);

var conceited = document.querySelector('.b326').innerHTML;
alert(conceited);

var businessLamp = document.querySelectorAll('.big');
for (var i = 0; i < businessLamp.length; i++) {
  console.log(businessLamp[i].innerHTML);
}

var conceitedKing = document.querySelectorAll('.container div');
  conceitedKing.forEach(function (e) {
    alert(conceitedKing);
});

var noBusiness = document.querySelectorAll('div.asteroid');
for (var i = 0; i < noBusiness.length; i++) {
  console.log(noBusiness[i].innerHTML);
}

var allBizniss = document.querySelector('p');
alert(allBizniss.innerHTML);
