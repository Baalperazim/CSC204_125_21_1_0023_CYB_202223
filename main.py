# Import the SingleLinkedList class from the linkedlists package
from linkedlists.singly_linked_list import SingleLinkedList

# Test the implementation
if __name__ == "__main__":
    # Create a new SingleLinkedList object
    linked_list = SingleLinkedList()

    # Test insert method with the given list [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]
    elements_to_insert = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    for element in elements_to_insert:
        linked_list.insert(element)

    # Test display method to see the linked list elements
    print("Linked List elements:")
    linked_list.display()

    # Test find_max_min method
    max_data, min_data = linked_list.find_max_min()
    print("Maximum data:", max_data)
    print("Minimum data:", min_data)

    # Test convert_to_bst method with a new linked list object
    new_linked_list = SingleLinkedList()
    new_linked_list.convert_to_bst([1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28])

    # Test display method to see the elements of the new linked list (BST)
    print("Binary Search Tree elements:")
    new_linked_list.display()