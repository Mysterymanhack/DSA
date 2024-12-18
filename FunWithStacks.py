#Program to implement stacks and perform various operations with them

class Node:
    """
    A node in a stack.

    Attributes:
    value
    next - link to next node
    """


    def __init__(self, value = None, next = None):
        ''' Creates a node with specified value.'''
        self.value = value
        self.next = next


class Stack:
    """
    A stack of nodes. Only the top node can be returned or modified

    Attributes:
    head
    """
    def __init__(self):
        '''Creates an empty stack'''
        self.head = None


    def push(self, value):
        '''Pushes a node with specified value onto the top of the stack'''
        new_node = Node(value = value, next = self.head)
        self.head = new_node
    

    def pop(self):
        '''Removes the top node'''
        node_being_deleted = self.head
        self.head = node_being_deleted.next
        value = node_being_deleted.value
        del node_being_deleted
        return value

    def peek(self):
        '''Returns the value of the top node'''
        return self.head.value


def nextGreatestElement(list):
    '''
    Returns the index of the next value greater than all elements of a given list.
    Returns -1 if none found.

    Parameter: list
    Returns: list
    '''
    stack = Stack()
    current = 0
    greatestList = [-1]*len(list)
    while current < len(list):
        if stack.head != None:
            while stack.head != None and stack.head.value[1] < list[current]:
                greatestList[stack.head.value[0]] = current
                stack.pop()
        stack.push([current,list[current]])
        current += 1
        print(stack.head.value)
    return greatestList

def lastLeastElement(list):
    '''
    Returns the index of the next value greater than all elements of a given list.
    Returns -1 if none found.

    Parameter: list
    Returns: list
    '''
    stack = Stack()
    current = len(list) - 1
    greatestList = [-1]*len(list)
    while current >= 0:
        if stack.head != None:
            while stack.head != None and stack.head.value[1] > list[current]:
                greatestList[stack.head.value[0]] = current
                stack.pop()
        stack.push([current,list[current]])
        current -= 1
    return greatestList
