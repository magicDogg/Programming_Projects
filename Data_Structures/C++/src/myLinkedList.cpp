// LinkedList Class Implementation in C++
// This is the cpp file

#include <stdio.h>
#include "LinkedList.h"


template <class T>
LinkedList<T>::LinkedList()
{
    head = NULL;
}

template <class T>
LinkedList<T>::~LinkedList()
{
    deleteAll();
}

template <class T>
void LinkedList<T>::insertAtHead(T n)
{
    Node<T>* temp = new Node<T>();
    temp->data = n;
    
    temp->next = head;
    head = temp;
}

template <class T>
void LinkedList<T>::removeAtHead()
{
    if (head == NULL)
    {
        cout << "Error: The List is already empty" << endl;
        return;
    }
    
    Node<T>* temp1 = head;
    Node<T>* temp = head;
    temp = temp->next;
    
    head = temp;
    delete temp1;
}

template <class T>
void LinkedList<T>:: insertAtTail(T n)
{
    if (head == NULL)
    {
        Node<T>* last = new Node<T>();
        last -> data = n;
        last -> next = NULL;
        
        head = last;
        
        return;
    }
    
    Node<T>* temp = head;
    
    while((temp->next) != NULL)
    {
        temp = temp->next;
        
    }
    
    Node<T>* last = new Node<T>();
    last -> data = n;
    
    
    last -> next = NULL;
    temp -> next = last;
}


template <class T>
void LinkedList<T>::removeFromTail()
{
    if (head == NULL)
    {
        cout << "Error: The List is already Empty"<< endl;
        return;
    }
    else if((head)->next == NULL)
    {
        delete head;
        head = NULL;
        return;
    }
    
    
    Node<T>* temp1 = head;
    Node<T>* temp2;
    
    while((temp1 -> next) != NULL)
    {
        temp2 = temp1;
        temp1 = temp1->next;
    }
    
    delete temp1;
    temp2 -> next  = NULL;
    
}

template <class T>
int LinkedList<T>::count()
{
    if (head == NULL)
    {
        return 0;
    }
    
    int countElement = 0;
    Node<T>* temp = head;
    
    while(temp != NULL)
    {
        temp = temp -> next;
        countElement++;
    }
    
    return countElement;
}
template <class T>
void LinkedList<T>:: insert(int n, T value)
{
    if (n > (count() + 1))
    {
        cout << "Error: Excceds size of the List" << endl;
        return;
    }
    
    if (n == 1)
    {
        Node<T>* newNode = new Node<T>();
        newNode->data = value;
        
        newNode -> next = head;
        head = newNode;
        
        return;
    }
    Node<T>* newNode = new Node<T>();
    newNode->data = value;
    
    Node<T>* temp = head;
    
    for (int i = 0; i < (n - 2); i++)
    {
        temp = temp->next;
    }
    
    newNode -> next = temp -> next;
    temp -> next = newNode;
}

template <class T>
void LinkedList<T>::reverse()
{
    Node<T>* current = head;
    Node<T>* nexT;
    Node<T>* prev = NULL;
    
    while(current != NULL)
    {
        nexT = current -> next;
        current->next = prev;
        prev = current;
        current = nexT;
    }
    
    head = prev;
}

template <class T>
void LinkedList<T>::remove(int n)
{
    if(n == 1)
    {
        Node<T>* temp = head;
        
        Node<T>* temp1 = head;
        temp1 = temp1 -> next;
        head = temp1;
        
        delete temp;
        
        return;
    }
    
    Node<T>* temp1 = head;
    Node<T>* temp2 = head;
    
    
    for(int i = 0; i < (n - 2); i++)
    {
        temp1 = temp1 -> next;
    }
    temp2 = temp1 -> next;
    temp1 -> next = temp2 -> next;
    delete temp2;
}

template <class T>
void LinkedList<T>::deleteAll()
{
    if (head == NULL)
    {
        return;
    }
    
    Node<T>* temp = head;
    Node<T>* temp1 = head;
    while (temp ->next != NULL)
    {
        temp1 = temp -> next;
        delete temp;
        temp = temp1;
        
    }
    head = NULL;
}

template <class T>
void LinkedList<T>::print()
{
    Node<T>* temp = head;
    while (temp != NULL)
    {
        cout << temp->data << endl;
        temp = temp->next;
    }
}
