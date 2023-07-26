# nodes/node.py

class Node:
    def __init__(self, data):
        """
        Initializes a new Node with the given data.

        Parameters:
        data (any): The data to be stored in the node.
        """
        # Store the data in the node.
        self.data = data

        # Initialize the link to the next node (initially None).
        self.next_node = None
