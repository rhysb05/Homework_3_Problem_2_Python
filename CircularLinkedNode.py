class CircularLinkedNode:
	

	# Default constructor for the node class.
	def __init__(self, value):
		
		self.value = value
		self.next = None
	
	# Getter for the data in the list
	def get_data(self):
		
		return self.val
	
	# Getter for the next ptr
	def get_next(self):
		
		return self.next
	
	# Setter fot the next value
	def set_next(self, _new_next):
	
		self.next = _new_next
		