#Program to implement queues and perform various operations with them

class Node:
    """
    A node in a queue or doubly linked list.

    Attributes:
    value
    next - link to next node
    previous - link to previous node
    """


    def __init__(self, value = None, next = None, previous = None):
        ''' Creates a node with specified value.'''
        self.value = value
        self.next = next
        self.previous = previous


class Queue:
    """
    A queue of nodes. Only the front node can be returned or removed. Nodes can only be added to back.

    Attributes:
    head
    tail
    """
    def __init__(self):
        '''Creates an empty queue'''
        self.head = None
        self.tail = None


    def isEmpty(self):
        '''Checks whether queue is empty'''
        if self.head == None and self.tail == None:
            return True
        else:
            return False


    def enqueue(self, value):
        '''Adds a node with specified value onto the back of the stack'''
        new_node = Node(value = value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail
            self.tail.previous = new_node
            self.tail = new_node.next
    

    def dequeue(self):
        '''Removes the front node and returns its value'''
        node_being_deleted = self.head
        self.head = node_being_deleted.previous
        value = node_being_deleted.value
        del node_being_deleted
        return value


    def peek(self):
        '''Returns the value of the front node'''
        return self.head.value
