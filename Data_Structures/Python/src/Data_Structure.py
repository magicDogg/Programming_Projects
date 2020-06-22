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
    def insert(self, data, prev=None, next=None):
        new_node = DoubleNode(data)
        # check if previous and next exist in list first, if they do, identify
        if self.search(prev) & self.search(next):
            found_prev = False
            found_next = False
            current_node = self.head
            while (found_prev and found_next) is False:
                if current_node.get_data() == prev:
                    prev_node = current_node
                    found_prev = True
                    next_node = current_node.get_next()
                    found_next = True
                else:
                    current_node = current_node.get_next()
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
            new_node.set_prev(prev_node)
            new_node.set_next(next_node)
            prev_node.set_next(new_node)
            next_node.set_prev(prev_node)


# Stack class
class Stack:
    # Constructor - Creating an empty queue
    def __init__(self):
        self.head = None

    # Insert the new data at the top of the stack
    def push(self, data):
        new_node = Node(data)
        # if stack is empty
        if self.head is None:
            self.head = new_node
            self.head.set_next(None)
        else:
            new_node.set_next(self.head)
            self.head = new_node
        
    # Remove + Return the data from the top of the stack
    def pop(self):
        old_head = self.head
        self.head = self.head.get_next()
        return old_head.get_data()

    # Return the data from the top of the stack without removal
    def top(self):
        return self.head.get_data()

    # Print all the elements from the stack - this method exists for debugging purpose
    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.get_data())
            current_node = current_node.get_next()


# Queue class
class Queue:
    # Constructor - Creating an empty queue
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert the new data at the front of the queue
    def enqueue(self, data):
        new_node = DoubleNode(data)
        # if queue is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.set_next(None)
            self.size()
        # if queue has only 1 node
        elif self.size() == 1:
            new_node.set_next(self.head)
            self.head = new_node
            self.tail.set_prev(new_node)
        # if queue has more than 1 node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

    # Remove + Return the data from the end of the queue
    def dequeue(self):
        # return data from end of queue (tail)
        old_tail = self.tail

        # if this is the last node in the queue
        if self.size() == 1:
            self.head = None
            self.tail = None
        # if there are more nodes in the queue
        else:
            # replace tail with prev node
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        return old_tail.get_data()

    # return size of queue
    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count = count+1
            current_node = current_node.get_next()
        return count

    # Return the data from the end of the queue without removal
    def get(self):
        return self.tail.get_data()

    # Print all the elements from the queue - this method exists for debugging purpose
    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.get_data())
            current_node = current_node.get_next()


# TreeNode class - node used for tree data structures
class TreeNode:
    # Constructor
    def __init__(self,current_val):
        self.current_val = current_val # current node
        self.left_child = None # Initialize child as Null
        self.right_child = None # Initialize child as Null
        self.parent = None # Initialize parent as Null

    def insert(self, data):
        if self.current_val == data:  # is current node same as inserted node just place to the left
            return self.left_child.insert(data)
        elif data < self.current_val:
            if self.left_child:  # if left child exists, insert data into left child (recursion)
                return self.left_child.insert(data)
            else:
                self.left_child = TreeNode(data)  # set data as the left_child to current_node
                return True
        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = TreeNode(data)
                return True

    def search(self, data):
        if data == self.current_val:  # check if current node matches
            print(self.current_val)
            # check if you should search left
        elif data < self.current_val:
            if self.left_child:  # check if left node exists
                return self.left_child.search(data)
            else:  # if left node doesn't exist
                print("Not found")
            # check if you should search right
        elif data > self.current_val:
            if self.right_child: # check if right node exists
                return self.right_child.search(data)
            else: # if right node doesn't exist
                print("not found")

    def min(self):
        while self.left_child:
            return self.left_child.min()
        print(self.current_val)

    def max(self):
        while self.right_child:
            return self.right_child.max()
        print(self.current_val)

    def height(self):
        if self.right_child and self.left_child:
            return 1 + max(self.right_child.height(), self.left_child.height())
        elif self.right_child:
            return 1 + self.right_child.height()
        elif self.left_child:
            return 1 + self.left_child.height()
        else:
            return 1

    def in_order(self):
        if self:
            if self.left_child:
                self.left_child.in_order()
            print(self.current_val)
            if self.right_child:
                self.right_child.in_order()

    def pre_order(self):
        if self:
            print(self.current_val)
            if self.left_child:
                self.left_child.pre_order()
            if self.right_child:
                self.right_child.pre_order()

    def post_order(self):
        if self:
            if self.left_child:
                self.left_child.post_order()
            if self.right_child:
                self.right_child.post_order()
            print(self.current_val)

    def level_order(self):
        q = Queue()
        q.enqueue(self)
        while not q.size() == 0:
            node = q.dequeue()
            if (node.left_child):
                q.enqueue(node.left_child)
            if (node.right_child):
                q.enqueue(node.right_child)
            print(node.current_val)

# Binary Search Tree class
class BST:
    # Constructor - Creating an empty BST
    def __init__(self):
        self.root = None

    # insert node into tree: O(height) time complexity
    def insert(self, data):
        # https://www.youtube.com/watch?v=YlgPi75hIBc is a good example of recursive insertion
        if not self.root: # Is the BST empty?
            self.root = TreeNode(data)
        else:
            self.root.insert(data) # self.root is Treenode object, so the .insert() will be the insert fun in Treenode

    # Search for the matching node throughout the BST: time complexity same as insert
    def search(self, data):
        if self.root:
            return self.root.search(data)
        else:
            print("Tree is empty")

    # Search for the right node contains the min value throughout the BST: time complexity same as insert
    def find_min(self):
        if self.root:
            return self.root.min()
        else:
            print("Tree is empty")

    # Search for the right node contains the max value throughout the BST: time complexity same as insert
    def find_max(self):
        if self.root:
            return self.root.max()
        else:
            print("Tree is empty")

    # Compute the height of the BST - Use recursion to implement: time complexity same as insert
    def find_height(self):
        if self.root:
            return self.root.height()
        else:
            print("Tree is empty")

    # Traverse through all the nodes in BST and print them sequentially through the lower depth + from left to right
    # Use Queue to implement: time complexity same as insert
    def level_order(self):
        if self.root:
            return self.root.level_order()
        else:
            print("Tree is empty")

    # Traverse through the BST pre_order - Use recursion to implement: time complexity same as insert
    def pre_order(self):
        if self.root:
            return self.root.pre_order()
        else:
            print("Tree is empty")

    # Traverse through the BST in_order - Use recursion to implement: time complexity same as insert
    def in_order(self):
        if self.root:
            return self.root.in_order()
        else:
            print("Tree is empty")

    # Traverse through the BST post_order - Use recursion to implement: time complexity same as insert
    def post_order(self):
        if self.root:
            return self.root.post_order()
        else:
            print("Tree is empty")


# vertex class used in graph class
class Vertex:
    # Constructor
    def __init__(self, id, weight):
        self.id = id  # string
        self.edges = [weight] # this is a list containing the vertex weight and all of the edges (vertex id's)


#  graph class with only vertex weight
class Graph:
    # Constructor
    def __init__(self):
        # adj_list dictionary with key equal to id of vertex, and value equal to a vertex object
        self.adj_list = {}

    def add_vertex(self, vertex_object):
        if vertex_object.id in self.adj_list:
            print("Vertex id already exists in graph. Vertex id's must be unique")
        else:
            self.adj_list[vertex_object.id] = vertex_object.edges

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1.id in self.adj_list and vertex_2.id in self.adj_list:
            vertex_1.edges.append(vertex_2.id)  # add vertex 2 to vertex 1 list of edges (neighbor vertex)
            vertex_2.edges.append(vertex_1.id)  # add vertex 1 to vertex 2 list of edges (neighbor vertex)
        elif vertex_1.id in self.adj_list:
            print(vertex_2.id+' is not a vertex in the graph')
        elif vertex_2.id in self.adj_list:
            print(vertex_1.id + ' is not a vertex in the graph')
        else:
            print('neither vertex is in this graph, what are you doing??')

    def print_graph(self):
        print(self.adj_list)


#  graph class with vertex and edgeweight
class WeightedEdgeGraph:
    # Constructor
    def __init__(self):
        # adj_list dictionary with key equal to id of vertex, and value equal to a vertex object
        self.adj_list = {}

    def add_vertex(self, vertex_object):
        if vertex_object.id in self.adj_list:
            print("Vertex id already exists in graph. Vertex id's must be unique")
        else:
            self.adj_list[vertex_object.id] = vertex_object.edges

    # add dict: {'neighbor vertex id': edge weight} to each vertex.edges list
    def add_edge(self, vertex_1, vertex_2, edge_weight):
        if vertex_1.id in self.adj_list and vertex_2.id in self.adj_list:
            vertex_1.edges.append({vertex_2.id:edge_weight})  # add vertex 2 to vertex 1 list of edges (neighbor vertex)
            vertex_2.edges.append({vertex_1.id:edge_weight})  # add vertex 1 to vertex 2 list of edges (neighbor vertex)
        elif vertex_1.id in self.adj_list:
            print(vertex_2.id+' is not a vertex in the graph')
        elif vertex_2.id in self.adj_list:
            print(vertex_1.id + ' is not a vertex in the graph')
        else:
            print('neither vertex is in this graph, what are you doing??')

    def print_graph(self):
        print(self.adj_list)





# directed graph class
class directed_graph:
    # Constructor
    def __init__(self):
        self.root = None
