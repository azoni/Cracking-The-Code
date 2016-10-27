from random import randint

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)

	def __getitem__(self, data):
		return str(self.data)

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, data):
		node = Node(data)

		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def remove(self, data):
		current = self.head
		if current.data == data:
			self.head = self.head.next
		while(current.next != None):
			if current.next.data == data:
				current.next = current.next.next
				break
			else:
				current = current.next

	def __str__(self):
		if self.head != None:
			index = self.head
			nodestore = [str(index.data)]
			while index.next != None:
				index = index.next
				nodestore.append(str(index.data))
			return "[" + ", ".join(nodestore) + "]"
		return "[]"
		
	def __getitem__(self, idx):
		if isinstance(idx, slice):		
			start = idx.start or 0
			if (start >= 0) and (idx.stop is None) and (idx.step is None or idx.step == 1):
				no_copy_needed=True
			else:
				length = len(self)
				start, stop, step = idx.indices(length)
				no_copy_needed = (stop == length) and (step == 1)
			if no_copy_needed:
				l = self
				for i in range(start): 
					if not l: 
						break
					l=l.tail
				return l
			else:
				if step < 1: 
					return LinkedList(list(self)[start:stop:step])
				else:
					return LinkedList(itertools.islice(iter(self), start, stop, step))
		else:       
			if idx < 0: 
				idx = len(self)+idx
			if not self: 
				raise IndexError("list index out of range")
			if idx == 0: 
				return self.head
			return self.tail[idx-1]

def randomLinkedList(length, min, max):
	linkedlist = LinkedList()
	for i in range(length):
		value = randint(min, max)
		linkedlist.add(value)
	return linkedlist

