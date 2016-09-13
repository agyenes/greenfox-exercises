'use strict';

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const decryptor = require('./decryptor.js')

app.use(express.static('./client'));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

app.post('/decode',function(req, res) {
  decryptor.decrypt(req.body.text, req.body.shift, function (result) {
    res.json(result);
  });
});

app.listen(3000);
