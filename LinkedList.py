class Node():
  """
  A node object that points.
  """
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList():
  """
  A single linked list implementation.
  """
  _size = 0
  
  def __init__(self, *args):
    """
    Initializes the list and any items

    Args:
      *args: tuple of items for list

    Returns None
    """
    self.head = None
    if len(args) > 0:
      for i in range(len(args)):
        self.add(args[i])

  def add(self, item):
    """
    Adds a new item to the list.

    Args:
      item: item to add
    
    Returns None
    """
    if self.head == None:
      self.head = Node(item)
    else:
      self.head = Node(item, self.head)
    self._size = self._size + 1

  def remove(self, item):
    """
    Removes the item from the list.

    Args:
      item: item to remove
    
    Returns item
    """
    previous = None
    node = self.head
    for i in range(1, self._size):
      if node.data == item:
        if previous == None:
          previous = self.head
        previous.next = node.next
      else:
        previous = node
        node = node.next

  def search(self, item):
    """
    Searches for the item in the list.

    Args:
      item: item to search for
    
    Returns True if item is in list else False
    """
    node = self.head
    for i in range(self._size):
      if node.data == item:
        return True
      node = node.next
    return False

  def get(self, index):
    """
    Gets the item in the list.

    Args:
      index: the index of the item
    
    Returns the item at the given index
    """
    if index > (self._size - 1):
      raise IndexError("index out of range")
    node = self.head
    for i in range(index):
      node = node.next
    return node.data

  def isEmpty(self):
    """
    Checks whether the list is empty.

    Returns True if empty else False
    """    
    if self._size == 0:
     return True
    else:
      return False

  def size(self):
    """
    Returns the number of items in the list.
    """
    return self._size

  def append(self, item):
    """
    Adds a new item to the end of the list.

    Args:
      item: item to add to list

    Returns None
    """
    node = self.head
    if self._size == 0:
      self.head = Node(item)
      self._size += 1
      return
    for i in range(self._size):
      if i == self._size-1:
        node.next = Node(item)
        self._size += 1 
        return
      node = node.next

  def index(self, item):
    """
    Finds the index of first occurence of item in list.
    
    Args:
      item: item to search for

    Returns index of item
    """
    node = self.head
    for i in range(self._size):
      if node.data == item:
        return i
      node = node.next
    raise ValueError("{val} is not in list".format(val=item))

  def insert(self, pos, item):
    """
    Adds a new item to the list at position pos.
    
    Args:
      pos: index position of new item
      item: item to add to list

    Returns None
    """
    previous = None
    node = self.head
    if pos > self._size:
      raise IndexError("index out of range")
    for i in range(self._size - 1):
      if i == pos:
        temp = Node(item)
        if previous == None:
          temp.next = self.head
          self.head = temp
        else:
          temp.next = node
          previous.next = temp
        self._size += 1
      previous = node
      node = node.next

  def pop(self, pos = None):
    """
    Removes the item at position pos or the last item if pos == None.

    Args:
      pos: index position of item to remove

    Returns item at position pos or last item
    """
    previous = None
    node = self.head
    if pos == None:
      pos = self._size - 1
    if self._size == 1:
      self.head = None
      self._size -= 1
      return node.data
    for i in range(pos + 1):
      if i == pos:
        item = node.data
        previous.next = node.next
        self._size -= 1
        return item
      previous = node
      node = node.next
