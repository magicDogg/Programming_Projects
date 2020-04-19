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

    def insert(self, data):
        new_node = Node(data)
        # if you are adding the first node (not self.head = True if self.head = None)
        if not self.head:
          self.head = new_node
          self.head.set_next(new_node)
        # if not adding first node
        else:
            new_node.set_next(self.head)
            current_node = self.head
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()
            #TODO: for some reason, changing 'current_node.next' also changes self.head.next (bc immutable object?)
            current_node.set_next(new_node)
            self.head = new_node



# Doubly Linked List class
class DoublyLinkedList:
    # code for doubly linked list
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
