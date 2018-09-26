from CircularLinkedNode import CircularLinkedNode


class CircularLinkedList(object):
	
	def __init__(self):
		
		self.size = 0
		self.head = None
		self.tail = None

	def insert_at_begin(self, _value):
		
		# Create a new node containing the new value
		new_node = CircularLinkedNode(_value)
		
		if self.size == 0:
			
			self.head = new_node
			self.tail = new_node
			new_node.next = self.head
			
		else:
			
			temp = self.head
			new_node.next = temp
			
		
		