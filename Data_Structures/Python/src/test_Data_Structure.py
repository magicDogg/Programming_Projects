# Test-bench for Data_Structure library
# You-Young Lee, Richard Fields

import Data_Structure as DS


# Test bench switch
test_mode = 'Doubly_Linked_List'


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
    mcll.print_all()

    # Test size of the list
    print(mcll.size())

    # Test delete - List should be 4, 2, 1, 0
    mcll.delete(3)
    mcll.print_all()

    # Test search
    print(mcll.search(1))
    print(mcll.search(3))


# Test Doubly Linked List
def test_doubly_linked_list():
    # mcll stands for my doubly linked list
    mdll = DS.DoublyLinkedList()

    # Test insert node when list is empty - List should be 1
    mdll.insert(1)
    mdll.print_all()

    # Test insert node before head - List should be 0,1
    mdll.insert(0,None,1)
    mdll.print_all()

    # Test insert node after tail - List should be 0,1,2
    mdll.insert(2,1,None)
    mdll.print_all()

    # Test insert node in between nodes - List should be 0,1,1.5,2
    mdll.insert(1.5,1,2)
    mdll.print_all()

    # Test size of the list - should be 4
    print(mdll.size())

    # Test delete - List should be 0,1,2
    mdll.delete(1.5)
    mdll.print_all()

    # Test search - should be True and then False
    print(mdll.search(1))
    print(mdll.search(1.5))


# Execute the switched test bench
if test_mode == 'Node':
    test_node()
elif test_mode == 'Linked_List':
    test_linked_list()
elif test_mode == 'Circular_Linked_List':
    test_circular_linked_list()
elif test_mode == 'Doubly_Linked_List':
    test_doubly_linked_list()

