#!python

import time

def time_it(func):
    # Made wth love by Ben :heart: - DS2.3
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start) * 10000) + ' ms\n')
        return result
    return wrapper

class LinkedListIterator:
    def __init__(self, linked_list):
        self._linked_list = linked_list
        self._index = 0
        self.current = self._linked_list.head
    
    def __next__(self):
        if self._index < self._linked_list.length_fast():
            result = self.current
            self.current = result.next
            self._index += 1
            return result.data
        raise StopIteration

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.count = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        return LinkedListIterator(self)

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    # @time_it
    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?
        Answer:
            Best: O(1) if the list has only 1 element
            Worst: O(n) because we have to traverse the entire list of n elements to get n
        """
        # TODO: Loop through all nodes and count one for each
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # @time_it
    def length_fast(self):
        return self.count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        Answer: O(1) because each step is an assignment, which is constant time
        """
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.count += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        Answer: O(1) because we do not have to traverse through the entire list to access head
        """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            # prev_head, self.head = self.head, new_node
            prev_head = self.head
            self.head = new_node
            new_node.next = prev_head
        self.count += 1

    def find(self, quality):
        """Return the first item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        Answer: O(1) if first element fulfills quality condition
        TODO: Worst case running time: O(???) Why and under what conditions?
        Answer: O(n), if quality is not True by the end of the list, we have transvered the whole list
        """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        current = self.head
        while not quality(current.data):
            current = current.next
            if current == None:
                return None
        return current.data

    # no need to reassign delete node's next, garbage collection
    def delete(self, item=None):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        Answer: O(1) if there are no nodes in the list or the head is equal to the value to be deleted
        TODO: Worst case running time: O(???) Why and under what conditions?
        Answer: O(n) if the value to be deleted is at the end of the list or the value was not found at all
        """
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        # if list is empty
        if self.count == 0:
            raise ValueError('No items in list')
        # if list has only one Node (has to be head)
        elif self.head.data == item and self.count == 1:
            self.head = None
            self.tail = None
        # if head's data is equal to item
        elif self.head.data == item:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
        else:
            current = self.head
            while current.data != item:
                prev = current
                current = current.next
                # if current reaches last Node
                if current is None:
                    raise ValueError('Item not found: {}'.format(item))
            new_next_node = current.next
            # if last Node's data equal to item
            if new_next_node is None:
                self.tail = prev
            current.next = None
            prev.next = new_next_node
        self.count -= 1

    def replace(self, item, new_value):
        current = self.head
        replace_node = Node(new_value)
        
        # if list is empty
        if self.count == 0:
            raise ValueError('No items in list')
        # if list has only one Node (has to be head)
        elif self.head.data == item and self.count == 1:
            self.head = replace_node
            self.tail = replace_node
        # if head's data is equal to item
        elif self.head.data == item:
            head_next = self.head.next
            self.head = replace_node
            self.head.next = head_next
        else:
            current = self.head
            while current.data != item:
                prev = current
                current = current.next
                # if current reaches last Node
                if current is None:
                    raise ValueError('Item not found. Abort replace.')
            current_next = current.next
            if current_next is None:
                self.tail = replace_node
            current = replace_node
            current.next = current_next
            prev.next = current