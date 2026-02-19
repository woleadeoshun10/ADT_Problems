"""
This is a LinkedList setup, using a dummy Node to prevent pointer exception
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.dummy = Node() #Create dummy node
        self.tail = self.dummy #Initially point to dummy
    
     #Append new Node
    def append(self,data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
    
     #Print the List
    def print(self):
        current = self.dummy.next
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
     
     #Search the List
    def search(self,data):
        current = self.dummy.next
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        print("Not Found")
        return -1

    # Delete from list
    def delete(self,data):
        prev = self.dummy  # Start from the dummy node
        current = self.dummy.next # First actual node (head)
        
        while current:
            if current.data == data: # Found the node to delete
                prev.next = current.next # Skip the current node
                if current == self.tail: # If we're deleting the last node
                    self.tail = prev # Move the tail pointer back
                return True # success
            prev = current
            current = current.next
        return False #not found
        
    #Insert at position
    def insert(self,data,position):
        new_node = Node(data)
        prev = self.dummy
        current = self.dummy.next
        index = 0
        
        while current and index < position:
            prev = current
            current = current.next
            index += 1
        prev.next = new_node
        new_node.next = current
        
        if new_node.next is None:
            self.tail = new_node
            



ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(5)
ll.append(92)

ll.print()           
print(ll.search(5))
ll.delete(30)
ll.print()      
ll.insert(30, 0)
ll.print()


"I didnt think I could write that myself. Not too hard"
