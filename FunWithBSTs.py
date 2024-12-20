#Program to implement binary search trees and perform various operations with them

class Node:
    """
    A node in a binary search tree.

    Attributes:
    value
    left - left node: lower value
    right - right node: higher value
    """


    def __init__(self, value = None, left = None, right = None):
        ''' Creates a node with specified value.'''
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    """
    A binary search tree. 

    Attributes:
    root
    """


    def __init__(self,root = None):
        '''Initializes an empty Binary Search Tree'''
        self.root = root
    

    def add_node(self,value):
        '''Adds a node with a specified value'''
        if self.root == None:
            self.root = Node(value = value)
            return None
        else:
            current_node = self.root
        while True:
            if value <= current_node.value:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value = value)
                    return None
            else:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value = value)
                    return None
    

    def sorted_list(self):
        """
        Returns a list of elements of a binary search tree by depth-first traversal
        """

        if self.root == None:
            return []
        if self.root.left:
            left_list = BinarySearchTree(self.root.left).sorted_list()
        else:
            left_list = []
        if self.root.right:
            right_list = BinarySearchTree(self.root.right).sorted_list()
        else:
            right_list = []
        return left_list + [self.root.value] + right_list        
        
