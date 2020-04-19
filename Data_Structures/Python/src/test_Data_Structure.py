# Test-bench for Data_Structure library
# You-Young Lee, Richard Fields

import Data_Structure as DS


# Test bench switch
test_mode = 'Circular_Linked_List'


# Test Node class
def test_node():
    a = DS.Node(1)
    b = DS.Node(3.14)
    c = DS.Node("I am the Ice King")

    print(a.get_data())
    print(b.get_data())
    print(c.get_data())


# Test Linked List class
def test_linked_list():
    # mll stands for my linked list
    mll = DS.LinkedList()

    # Test insert node - List should be 4, 3, 2, 1, 0
    for i in range(0, 5):
        mll.insert(i)
    mll.print_all()

    # Test size of the list
    print(mll.size())

    # Test delete - List should be 4, 2, 1, 0
    mll.delete(3)
    mll.print_all()

    # Test search
    print(mll.search(1))
    print(mll.search(3))

# Test Circular Linked List
def test_circular_linked_list():
    # mcll stands for my circular linked list
    mcll = DS.CircularLinkedList()

    # Test insert node - List should be 4,3,2,1,0
    for i in range(0, 5):
        mcll.insert(i)
    print(mcll.size())
    # put test code here

# Test Doubly Linked List
def test_doubly_linked_list():
    print('something')
    # put test code here

# Execute the switched test bench
if test_mode == 'Node':
    test_node()
elif test_mode == 'Linked_List':
    test_linked_list()
elif test_mode == 'Circular_Linked_List':
    test_circular_linked_list()
elif test_mode == 'Doubly_Linked_List':
    test_doubly_linked_list()

