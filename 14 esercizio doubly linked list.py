#!/usr/bin/python3

from platform import java_ver


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        if self.length == 0:
            print(None)

    def append(self, value):
        new_node = Node(value)
        if self.length == 0: # se non c'è un return statement dentro l'if serve un elif o un else
            self.head = new_node
            self.tail = new_node
        else: # mi sono dimenticato else
            self.tail.next= new_node
            new_node.prev = self.tail # avevo scritto self head
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1: 
            self.head = None
            self.tail = None
        else:
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return temp

# def get, set, insert, remove

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length//2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        if index >= self.length//2:
            temp = self.tail
            for _ in range(self.length -1, index, -1): # ricordare questa logica di range
                temp = temp.prev
        return temp

    def set_value(self, value, index):
        temp= self.get(index)
        if temp:
            temp.value = value
            return print(temp.value)
        return print('index out of range')
        #if index < 0 or index > self.lenght:
            #return False
        #temp = self.get(index)
        #temp.value = value
        #return True

    def insert(self, value, index):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return print('index out of range')
        if index == 0:
            return self.pop_first()
        elif index == self.length -1: 
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None
        self.lenght -= 1
        return temp



my_doubly_linked_list = DoublyLinkedList(10)

my_doubly_linked_list.append(20)
my_doubly_linked_list.append(30)


my_doubly_linked_list.print_list()

my_doubly_linked_list.set_value(100, 0)

my_doubly_linked_list.insert(5,3)

my_doubly_linked_list.remove(4)

my_doubly_linked_list.print_list()


