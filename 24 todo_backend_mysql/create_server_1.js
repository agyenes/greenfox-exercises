'use strict';

var http = require('http');

var server = http.createServer(function(req, res) {
  var date = new Date();
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end(req.url + ' ' + req.method + ' ' + date);
});

server.listen(3000, '127.0.0.1');
