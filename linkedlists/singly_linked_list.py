# Import the Node class from the nodes package
from nodes.node import Node

# Define the SingleLinkedList class
class SingleLinkedList:
    def __init__(self):
        self.head = None  # Initially, the linked list is empty, so the head points to None

    def insert(self, data):
        # Method to insert a new node with the given data at the end of the linked list
        new_node = Node(data)  # Create a new node with the given data

        if self.head is None:
            # If the linked list is empty, make the new node the head of the list
            self.head = new_node
        else:
            # Otherwise, traverse the list to find the last node and link the new node to it
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        # Method to display the elements of the linked list
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        print(elements)
