# Import the Queue class from the linkedlists package
from linkedlists.singly_linked_list import Queue

# Import the binary_search_unsorted function from the binary_search module
from binary_search import binary_search_unsorted

# Test the implementation
if __name__ == "__main__":
    # Test Queue data structure using a single linked list
    queue = Queue()

    # Test enqueue method
    queue.enqueue(3)
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(2)

    # Test display method to see the elements in the queue
    print("Queue elements:")
    queue.display()

    # Test dequeue method
    dequeued_element = queue.dequeue()
    print("Dequeued element:", dequeued_element)

    # Test display method after dequeuing
    print("Queue elements after dequeuing:")
    queue.display()

    # Test sorting the queue
    queue.sort()

    # Test display method after sorting
    print("Queue elements after sorting:")
    queue.display()

    # Test binary search on an unsorted array
    unsorted_array = [3, 1, 4, 2, 8, 7, 5]
    target = 4
    index = binary_search_unsorted(unsorted_array, target)
    print(f"Index of {target} in the unsorted array:", index)
