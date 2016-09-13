'use strict';

var tape = require('tape');
var myFunction = require('./01');

tape(function (t) {
    t.deepEqual(myFunction('apple'), {a: 1, p: 2, l: 1, e: 1});
    t.end();
});

tape(function (t) {
    t.deepEqual(myFunction('aple'), {a: 1, p: 1, l: 1, e: 1});
    t.end();
});

tape(function (t) {
    t.deepEqual(myFunction(4), {4: 1});
    t.end();
});
