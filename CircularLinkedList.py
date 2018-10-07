from CircularLinkedNode import CircularLinkedNode


class CircularLinkedList(object):
	
	def __init__(self):
		
		self.size = 0
		self.head = None
		self.tail = None
		
	# end constructor

	def insert_at_begin(self, _value):
		
		# Create a new node containing the new value
		new_node = CircularLinkedNode(_value)
		
		if self.size == 0:
			
			self.head = new_node
			self.tail = new_node
			new_node.next = self.head
			
		else:
			
			new_node.next = self.head
			self.tail.next = new_node
			
		# Increment the size of the list
		self.size += 1
		
		
	# end insert_at_begin
	
	# This function inserts a node at the end of the list
	def insert_at_end(self, _value):
		
		if self.size == 0:
			
			self.insert_at_begin(_value)
			
		# end if
	
		else:
			
			# Create new node
			new_node = CircularLinkedNode(_value)
			
			# Assign the tail pointer to the new node
			self.tail.next = new_node
			
			# Make the newly created node the tail pointer
			self.tail = new_node
			
			# Make the new tail node point to the head of the list
			self.tail.next = self.head
			
			self.size += 1
		# end else
		
		print("The value", _value, "has been added to the list.\nv")
		
		
		
	# end insert_at_end()
	
	# This function inserts an element at the desired
	# index position in our list.
	
	def insert_at_element(self, _index, _value):
		
		feedback = _index
		
		# If the index entered is past the limit of our list
		if _index + 1 > self.size:
			
			print("That index position is too large silly!!")
			
		# end if
		
		# Set the cursor node to the position of the head node
		cursor_node = self.head
		
		# If the index position is 0
		if _index == 0:
			
			self.insert_at_begin(_value)
		
		# end if
		
		# This while loop places the cursor at the desired position
		# to perform the insertion.
		while _index - 3 > -1:
			
			# Move the cursor to the next node
			cursor_node = cursor_node.next
			# Decrease the index number until our
			# cursor is pointed at the right position.
			_index -= 1
			
		# end while
		
		# Create a new node to be inserted into the list
		insert_node = CircularLinkedNode(_value)
		
		# Set the next value of the new node.
		insert_node.next = cursor_node.next.next
		
		# Ensure that the node before the newly inserted node is pointing
		# to our newly inserted node.
		cursor_node.next.next = insert_node
		
		print("Node has been added at position", feedback, "with a value of", _value)
		
		self.size += 1
		
	# end insert_at_index
	
	def get_element_at(self, _index):
		
		# If the index entered is past the size of the list
		if _index + 1 > self.size:
			
			print("That index position is too large silly!!")
		
		# end if
		
		new_node = self.head
		
		# Iterate over the list until we reach the
		# appropriate index position.
		
		while _index - 1 != -1:
			
			# Move the cursor to the next node
			new_node = new_node.next
			# Decrease the index value
			_index -= 1
			
		# end while
		
		return new_node.value
	
	# end get_element_at()

	
	def print_list(self):
		
		# Create a node to act as the cursor
		cursor_node = self.head
		
		# If the list is empty
		if self.size <= 0:
			
			print("The list is empty silly")
			
		# end if
		
		else:
			# Print out each element in the list
			for i in range(self.size):
				
				print("{0}".format(cursor_node.value))
				cursor_node = cursor_node.next
				
		# end else
		
		print("\n")
	# end print_linked_list()

	# This function gets the size of the list
	
	
	# This function shifts all elements in the list by one
	# in the counter-clockwise direction.
	
	
	def shift_counter_clockwise(self):
		
		self.head = self.head.next
	
	# end shift_counter_clockwise()

	# This function shifts all elements in the list by
	# one in the clockwise direction.
	
	
	def shift_clockwise(self):
		
		for i in range(self.size - 1):
			
			self.head = self.head.next
			
		# end for i in range (self.size)

