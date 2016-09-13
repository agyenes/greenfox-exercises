'use strict';

var tape = require('tape');
var decryptor = require('./decryptor');

tape(function (t) {
    t.deepEqual(decryptor("oruhp lsvxp groru 456 vlw", 3), ("lorem ipsum dolor 456 sit"));
    t.end();
});

tape(function (t) {
    t.deepEqual(decryptor("lorem ipsum dolor sit", 0), ("lorem ipsum dolor sit"));
    t.end();
});

tape(function (t) {
    t.deepEqual(decryptor("", 5), (""));
    t.end();
});

tape(function (t) {
    t.deepEqual(decryptor("oruhp LSVXP GRO <># 456 vlw", 3), ("lorem IPSUM DOL <># 456 sit"));
    t.end();
});
