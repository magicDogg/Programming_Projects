import Data_Structure as DS


test_mode = 'Linked_List'

if test_mode == 'Linked_List':
    # mll stands for my linked list
    mll = DS.LinkedList()

    # Test insert node - List should be 4, 3, 2, 1, 0
    for i in range(0, 5):
        mll.insert(i)
    mll.print_all()

    # Test size of the list
    print mll.size()

    # Test delete - List should be 4, 2, 1, 0
    mll.delete(3)
    mll.print_all()

    # Test search
    print mll.search(1)
    print mll.search(3)
