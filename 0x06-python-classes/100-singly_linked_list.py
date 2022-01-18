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
        return(self.__data)
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
            llstr += str(itr.__data) + '-->'
            itr = itr.__next_node
            print(llstr)
        return llstr
    """insertar nodos la funcion"""
    def sorted_insert(self, value):
        print("entered sorted", end='')
        node = Node(value, self.__head)
        print(node.data)
        self.__head = node
