class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
    
  def push(self, data):
    new_node = Node(data)
    if self.top:
      new_node.next = self.top
    
    self.top = new_node
    
    self.size += 1

  def pop(self):
    if self.top is None:
        return None
    else:
        popped_node = self.top
    self.size -= 1
    self.top = self.top.next
    popped_node.next = None
    return popped_node.data

# You can also use this module which is a built in Stack
import queue

# Create an infinite LifoQueue
my_book_stack = queue.LifoQueue(maxsize=0)

# Add 
my_book_stack.put("Don Quixote")

# Remove
my_book_stack.get()