class Stack(object):

  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    return self.stack.pop(0)

  def peek(self):
    return self.stack[-1]

  def isEmpty(self):
    return self.stack == []

  def size(self):
    return len(self.stack)