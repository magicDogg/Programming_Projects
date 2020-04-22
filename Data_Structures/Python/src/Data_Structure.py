# Self-implementing data structure practice library
# You-Young Lee, Richard Fields


# Node class - Data block that contains the data + points the next node block
class Node:
    # Constructor
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

    # Get the data belongs to the node
    def get_data(self):
        return self.data

    # Set next toward the different node
    def set_next(self, new_next):
        self.next = new_next

    # Get the node that is pointed by next
    def get_next(self):
        return self.next


# DoubleNode class - Data block that contains data + points to the next & previous block
class DoubleNode:
    # Constructor
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null

    # Get the data belongs to the node
    def get_data(self):
        return self.data

    # Set next toward the different node
    def set_next(self, new_next):
        self.next = new_next

    # Set prev toward the different node
    def set_prev(self, new_prev):
        self.prev = new_prev

    # Get the node that is pointed by next
    def get_next(self):
        return self.next

    # Get the node that is pointed by prev
    def get_prev(self):
        return self.prev


# Linked List class
class LinkedList:
    # Constructor - Merely creating an empty linked list
    def __init__(self):
        self.head = None

    # Insert the new node at the beginning of the Linked List
    # Time complexity: O(1) <Linked List< vs. O(n) <Array>, where n is proportional to the size of the container
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # Count how many nodes are in the linked list
    # Time complexity: O(n) <Linked List> vs. O(1) <Array>
    def size(self):
        current_node = self.head
        count = 0

        while current_node:
            count += 1
            current_node = current_node.get_next()

        return count

    # Search the matching node throughout the linked list
    # Time complexity: O(n) <We are most likely to find the desired node at n/2 index by prob where n is # of nodes>
    # For search function, time complexity of Array search and Linked List search are both O(n)
    def search(self, data):
        current_node = self.head
        found = False

        while current_node and found is False:
            if current_node.get_data() == data:
                return True
            else:
                current_node = current_node.get_next()

        if current_node is None:
            return False

    # Delete the matching node from the linked list
    # Time complexity: O(n) <We have to "search" the right node to delete it>
    def delete(self, data):
        current_node = self.head
        previous = None
        found = False

        while current_node and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                previous = current_node
                current_node = current_node.get_next()

        if current_node is None:
            raise ValueError("Data not in list")

        if previous is None:
            self.head = current_node.get_next()
        else:
            previous.set_next(current_node.get_next())

    # Print all for debugging purpose
    def print_all(self):
        current_node = self.head

        while current_node:
            print(current_node.get_data())
            current_node = current_node.get_next()


# Circular Linked List class (derived class from LinkedList parent class)
class CircularLinkedList(LinkedList):
    # keep (use inheritance): init
    # change (use polymorphism): insert
    # Constructor - Merely creating an empty linked list
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.tail)
        current_node = self.head
        # if the list is empty
        if current_node is None:
            self.head = new_node
            self.head.set_next(self.tail)
        # if the list is not empty
        else:
            new_node.set_next(self.head)
            self.head = new_node


# Doubly Linked List class
class DoublyLinkedList(LinkedList):
    # code for doubly linked list
    # Constructor - Merely creating an empty linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # if you assign a val to an arg, it sets as default if user doesn't input val
    def insert(self, data, prev = None, next = None):
        new_node = DoubleNode(data)
        prev_node = prev
        next_node = next
        # if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.set_prev(None)
            self.head.set_next(None)
        # if list not empty and add node before head
        elif next is self.head.get_data():
            self.head.set_prev(new_node)
            new_node.set_next(self.head)
            self.head = new_node
        # if list not empty and add node after tail
        elif prev is self.tail.get_data():
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node
        # if list not empty and add node in between head and tail
        else:
            new_node.set_prev(prev)
            new_node.set_next(next)


# Stack class
class Stack:
    # Constructor - Creating an empty stack
    def __init__(self):
        self.tail = None

    # Insert the new data at the top of the stack
    def push(self, data):
        print("I am the Ice King")
        new_node = DoubleNode(data)
        
    # Remove + Return the data from the top of the stack
    def pop(self):
        print("I am the Ice King")

    # Return the data from the top of the stack without removal
    def top(self):
        print("I am the Ice King")

    # Print all the elements from the stack - this method exists for debugging purpose
    def print_all(self):
        print("I am the Ice King")


# Queue class
class Queue:
    # Constructor - Creating an empty queue
    def __init__(self):
        self.head = None

    # Insert the new data at the front of the queue
    def enqueue(self, data):
        print("I am the Ice King")

    # Remove + Return the data from the end of the queue
    def dequeue(self):
        print("I am the Ice King")

    # Return the data from the end of the queue without removal
    def get(self):
        print("I am the Ice King")

    # Print all the elements from the queue - this method exists for debugging purpose
    def print_all(self):
        print("I am the Ice King")
