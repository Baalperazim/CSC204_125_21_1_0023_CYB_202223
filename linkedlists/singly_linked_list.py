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


# Define the Queue class using the SingleLinkedList class
class Queue:
    def __init__(self):
        self.queue = SingleLinkedList()

    def enqueue(self, data):
        # Method to add an element to the rear of the queue (linked list)
        self.queue.insert(data)

    def dequeue(self):
        # Method to remove the front element from the queue (linked list)
        if self.is_empty():
            return None
        front_data = self.queue.head.data
        self.queue.head = self.queue.head.next
        return front_data

    def is_empty(self):
        # Method to check if the queue is empty
        return self.queue.head is None

    def display(self):
        # Method to display the elements of the queue (linked list)
        self.queue.display()
