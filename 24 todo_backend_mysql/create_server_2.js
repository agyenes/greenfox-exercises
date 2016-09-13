var express = require('express');
var http = require('http');
var app = express();

app.get('/', function(req, res) {
  var date = new Date();
  res.send(req.url + ' ' + req.method + ' ' + date + 'method: ' + req.method);
});

app.listen(3000);
