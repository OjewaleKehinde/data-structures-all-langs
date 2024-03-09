from ...linkedlist.doubly.python.DoublyLinkedList import DoublyLinkedList

"""
Implementation of a queue using a doubly linked list
"""
class ElementNotFoundError(Exception):
    """Exception raised when an element is not found."""

    def __init__(self, message):
        self.message = message

class queue:
    def __init__(self):
        self.linkedlist = DoublyLinkedList
        
    #Adds an element to the front of the queue
    def enqueue(self, element: any) -> None:
        """
        This method adds an element to a queue
        :param element: This represents the element to be added to the queue.
        """
        self.linkedlist.addFirst(element)
        
    #Removes the element at the front of the queue
    def dequeue(self) -> None:
        if not self.linkedlist.head:
            raise ElementNotFoundError('Cannot remove element from empty queue')   
    
    # Retrieves element at the front of the queue
    def peek(self) -> any:
        if not self.linkedlist.head:
            raise ElementNotFoundError('Element does not exist')
        return self.linkedlist.peek()
