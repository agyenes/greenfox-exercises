'use strict';

var express = require('express');
var http = require('http');
var app = express();
var bodyParser = require('body-parser');
var id = 0;
var mongodb = require('mongodb');
var MongoClient = mongodb.MongoClient;
var url = 'mongodb://localhost:27017/todos';

MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    console.log('Connection established to', url);
    db.close();
  }
});

app.use(express.static(__dirname + '/frontend/'));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

app.use(function (req, res, next) {
 res.contentType('application/json');
 next();
});

app.get('/todos', function(req, res) {
  MongoClient.query('db.restaurants.find()',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(rows);
  })
});

app.get('/todos/:id', function(req, res) {
  con.query('SELECT * FROM todos WHERE id = ?;', req.params.id, function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    var id = rows[0].id;
    var text = rows[0].text;
    var completed = rows[0].completed;
    res.send(JSON.stringify({
      'id': id,
      'text': text,
      'completed': completed
    }));
  })
});

app.post('/todos', function(req, res) {
  con.query('INSERT INTO todos (text) VALUES (?)', req.body.text, function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(JSON.stringify({
      'id': rows.insertId,
      'text': req.body.text,
      'completed': false
    }));
  })
});

app.put('/todos/:id', function(req, res) {
  con.query('UPDATE todos SET text = ?, completed = ? WHERE id = ?;', [req.body.text, req.body.completed, req.params.id], function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(JSON.stringify({
      'id': req.params.id,
      'text': req.body.text,
      'completed': req.body.completed
    }));
  })
});

app.delete('/todos/:id', function(req, res) {
  con.query('SELECT text FROM todos WHERE id = ?;', req.params.id, function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    var deleted_text = rows[0].text;
    con.query('DELETE FROM todos WHERE id = ?;', req.params.id, function(err,rows){
      if(err) {
        console.log(err.toString());
        return;
      }
      res.send(JSON.stringify({
        'id': req.params.id,
        'text': deleted_text,
        'completed': true,
        'destroyed': true
      }));
    })
  });
});


app.listen(3000);
