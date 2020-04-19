// LinkedList Class Implementation in C++
// This is the header file

#ifndef LinkedList_h
#define LinkedList_h

#include <iostream>
using namespace std;

template <typename T>
struct Node
{
    T data;
    Node* next;
};

template <typename T>
class LinkedList
{
private:
    Node<T>* head;
    
public:
    
    LinkedList();
    
    ~LinkedList();
    
    void insertAtHead(T n);

    void removeAtHead();
    
    void insertAtTail(T n);
    
    void removeFromTail();
    
    int count();
    
    void insert(int n, T value);

    void reverse();
    
    void remove(int n);
    
    void deleteAll();
    
    void print();

};

#endif /* LinkedList_h */
