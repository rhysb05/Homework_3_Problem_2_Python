from CircularLinkedNode import CircularLinkedNode
from CircularLinkedList import CircularLinkedList

my_list = CircularLinkedList()

test = CircularLinkedNode(7)


# Insert five elements into the list
my_list.insert_at_end(0)
my_list.insert_at_end(1)
my_list.insert_at_end(2)
my_list.insert_at_end(3)
my_list.insert_at_end(4)

# Print current list.

my_list.print_list()

# Add an element at index position 4
my_list.insert_at_element(4, 35)

# print current list
my_list.print_list()

# Shift the list by one in the counterClockwise direction
my_list.shift_counter_clockwise()
print("We have shifted the list by one in the counter-clockwise direction.")

# print current list
my_list.print_list()

# Shift the list by one in the counterclockwise direction.
my_list.shift_clockwise()
print("We have shifted the list by one in the clockwise direction.")

# print current list
my_list.print_list()

