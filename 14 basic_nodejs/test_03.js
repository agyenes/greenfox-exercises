'use strict';

var tape = require('tape');
var myFunction = require('./03');
var rectangle1 = new myFunction.Rectangle(5, 6);
var rectangle2 = new myFunction.Rectangle(4, 7);

tape(function (t) {
    t.equal(rectangle1.getArea(), 30);
    t.end();
});

tape(function (t) {
    t.equal(rectangle1.getCircumference(), 22);
    t.end();
});

tape(function (t) {
    t.equal(rectangle2.getArea(), 28);
    t.end();
});

tape(function (t) {
    t.equal(rectangle2.getCircumference(), 22);
    t.end();
});
