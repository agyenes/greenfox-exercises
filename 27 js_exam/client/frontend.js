'use strict';

var url = 'http://localhost:3000/';
var button = document.querySelector('#submit');
var response = document.querySelector('p');
var inputtext = document.querySelector('#sentence').value;
var shift = document.querySelector('#number').value;
var inputdata = {
  "text": inputtext,
  "shift": shift
}

button.addEventListener("click", submit);

function displayResponse(response) {
  var item = JSON.parse(response);
  var responseField = document.querySelector('.response');
  response.innerHTML(xhr.responseText);
}

function submit(e){
  e.preventDefault();
  if (inputtext.value ==='') {
    alert('Please enter a code to decrypt!');
  } else if (shift.value ==='') {
    alert('Please enter a number to shift!');
  } else if (typeof.shift.value !== int) {
    alert('Invalid shift value!');
  } else {
    decryptData(JSON.stringify(inputtext()),function(response) {
      displayResponse(response);
    }
    inputtext.value = '';
    shift.value = '';
  )}
}

function addEncryptedCode(inputdata, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', host);
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.send(JSON.stringify({'inputtext' : inputdata.text},{'shift' : inputdata.shift}));
  xhr.onload = function() {
    if (xhr.readyState === xhr.DONE) {
      var DecryptedCode = JSON.parse(xhr.response);
      callback(DecryptedCode);
    };
  };
}
