#!/usr/bin/python3
"""linked list"""


class Node:
    """class node atributos data y nextnode"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    """getter data"""
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        self.__next_node = value
"""class linked list"""


class SinglyLinkedList:
    """atributo head of the linked list"""
    def __init__(self):
        self.__head = None
    """linked list printeable"""
    def __str__(self):
        if self.__head is None:
            print('empty')
            return
        itr = self.__head
        llstr = ''
        while itr:
            llstr += str(itr.data)
            if itr.next_node:
                llstr+= '\n'
            itr = itr.next_node
        return llstr
    """insertar nodos la funcion"""
    def sorted_insert(self, value):
        node = Node(value, None)
        if self.__head == None:
            self.__head = node
        else:
            tmp = self.__head
            while(self.__head.next_node and self.__head.data > value):
                self.__head = self.__head.next_node
            self.__head.next_node = node
            self.__head = tmp

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
