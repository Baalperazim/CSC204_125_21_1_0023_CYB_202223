# Import the SingleLinkedList class from the linkedlists package
from linkedlists.singly_linked_list import SingleLinkedList

# Test the implementation
if __name__ == "__main__":
    # Create an instance of SingleLinkedList
    linked_list = SingleLinkedList()

    # Test insert method with the given list [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]
    elements_to_insert = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    for element in elements_to_insert:
        linked_list.insert(element)

    # Test display method to see the linked list elements
    linked_list.display()


#Explanation