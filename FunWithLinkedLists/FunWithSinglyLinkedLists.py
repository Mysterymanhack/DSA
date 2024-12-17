#Definition of a node
class Node:

    #Creates a node with a specified value that is not pointing to anything.
    def __init__(self,value,**kwargs):
        self.value = value
        self.next = kwargs.get('nextNode',None)


#Creates a new node at the start of the linked list and makes it the head
def insertNodeAtStart(value,Head):
    newNode = Node(value = value, nextNode = Head)
    return newNode

#Traverses the linked list and returns every value in the list
def traverseList(Head):
    currentNode = Head
    unLinkedList = []
    while currentNode != None:
        unLinkedList.append(currentNode.value)
        currentNode = currentNode.next
    return unLinkedList

#Creates a new node at the end of the list
def insertNodeAtEnd(value,Head):
    currentNode = Head
    while currentNode.next != None:
        currentNode = currentNode.next
    currentNode.next = Node(value = value)

#Creates a new node after a given node
def insertAfterNode(value,node):
    newNode = Node(value = value, nextNode = node.next)
    node.next = newNode
    return newNode

#Deletes the next node of a given node
def deleteNextNode(node):
    nodeBeingRemoved = node.next
    node.next = node.next.next
    del nodeBeingRemoved
