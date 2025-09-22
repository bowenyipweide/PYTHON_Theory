class Node:
    def __init__(self, data, next):
    self.data = data
    self.next = next
    
"""Implementation of a linked list"""
class LinkedList:
    def __init__(self):
            self.head = None

"""Display each element in the linked list"""
def display(self):
    current = self.head
    while current:
        print(current.data, end=" -> ") # the format of printing depends on the problem
        current = current.next
    print("None")
"""Search the node at index i"""
def findAt(self, index):
    current = self.head
    if not current:
        return None
    while index>0:
        current = current.next
        if not current:
            return None
        index-=1
    return current

