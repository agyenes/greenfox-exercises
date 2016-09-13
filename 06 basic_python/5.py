# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():
  def __init__(self):
    self.elements = []
    self.length = 0

  def size(self):
    return self.length

  def push(self, number):
    self.elements += [number]
    self.length += 1
    return self.length

  def pop(self):
    a = self.elements[self.length - 1]
    new_list = []
    for i in range(0, self.length - 1):
      new_list += [self.elements[i]]
    self.length -= 1
    self.elements = new_list
    return a

stack1 = Stack()

stack1.push(4)
stack1.push(3)
stack1.push(5)
stack1.push(2)

print(stack1.size())
print(stack1.pop())
print(stack1.elements)
print(stack1.pop())
print(stack1.size())
