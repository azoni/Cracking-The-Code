from LinkedList import *

#Hash
def deleteDup(linkedList):
	if (linkedList.head != None):
		current = linkedList.head
		table = {current.data: True}
		while current.next != None:
			if current.next.data in table:
				current.next = current.next.next
			else:
				table[current.next.data] = True
				current = current.next

#no data strucutures
#def deleteDup2

if __name__ == '__main__':
	linkedList = randomLinkedList(10, 4, 6)
	deleteDup(linkedList)
	print linkedList