'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack() {
  this.stack = [],
  this.stack_index = 0,
  this.size = function(){
    return this.stack_index;
  },
  this.push = function(element){
    this.stack[this.stack_index] = element;
    this.stack_index++
  },
  this.pop = function(element){
    var last_item = this.stack[this.stack_index-1];
    this.stack = this.stack.slice(0,this.stack_index-1);
    this.stack_index--
  }
}

var myStack = new Stack();

myStack.push('black')
myStack.push('box')
myStack.push('recorder')
console.log(myStack.stack);
console.log(myStack.size());
myStack.pop('box')
console.log(myStack.size());
console.log(myStack.stack);
