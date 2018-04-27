#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:51:13 2018

@author: xingyichong
"""

# linked list

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedlist:
'''
Linked list class:
----------
Attr: head
Method: len(), Insert(), index()

'''
    def __init__(self):
        self.head = None
        
    def len(self):  # return the length of list
        cur_node = self.head
        length = 0
        while cur_node != None:
            length += 1
            cur_node = cur_node.next
        return length
            
    def Insert(self, newNode, position = -1):  # Insert one node in a given position
        # position = -1: insert at the end. (Default)
        # position = 0: insert at the head
        # position > 0: insert after this position 
        
        if type(position) != int :
            raise TypeError('Index must be an integer!')
        if position < -1 :
            raise ValueError('Index cannot < -1!')
        
        if self.head == None:
            self._insert_inemptylist(newNode)
            return
            
        if position == 0:
            self._insert_head(newNode)
        elif position == -1:
            self._insert_mid(newNode, -1)
        else:
            self._insert_mid(newNode, position)
    
### private funtion for inserting    
    def _insert_inemptylist(self,newNode):
        self.head = newNode
    
    def _insert_head(self, newNode):
        self.head, self.head.next = newNode, self.head
        
    def _insert_mid(self, newNode, position):
        lenoflist = self.len()
        
        if position > lenoflist:
            raise ValueError('Index of the list is beyond the length of the list.')
            
        if position == -1:
            cur_node = self.index(lenoflist)
            cur_node.next = newNode
        else:
            cur_node = self.index(position)
            oldnext_node=cur_node.next
            
            cur_node.next, newNode.next = newNode, oldnext_node
####
            
    def index(self, position):  # return the node for a given index
        if position < 0:
            raise ValueError('Index of the list cannot be negative')
            
        if position == 0: return None
        
        cur_pos, cur_node = 1, self.head
        
        while cur_pos != position:
            cur_pos += 1
            cur_node = cur_node.next
        
        return cur_node
    

    def __str__(self):
        cur_node = self.head
        if cur_node == None:
            str_toprint = 'This linked list is empty!'
        else:
            str_toprint = 'Below,the linked list data: ' + '\n===================\n'
            while cur_node != None:
                str_toprint += str(cur_node.data)
                str_toprint += '\n'
                cur_node = cur_node.next
                
        return str_toprint
        
            
##################
def test():
    firstn = node('first')
    link = linkedlist()
    print('\n---Test creating a empty list:')
    print(link)
    print('**Length**: ', link.len())

    
    
    link.Insert(firstn)
    print('\n---Test to insert the first value into an empty list:')
    print(link)
    print('**Length**: ', link.len())

    for i in range(5):
        link.Insert(node(i))
    print('\n---Test to insert in the end:')
    print(link)
    print('**Length**: ', link.len())
    
    
    N = 2
    link.Insert(node('j'),N)
    print('\n---Test to insert "j" after position ' + str(N) + ':')
    print(link)
    print('**Length**: ', link.len())
    
    link.Insert(node('new'),0)
    print('\n---Test to insert "new" at head:')
    print(link)
    print('**Length**: ', link.len())
    
    link.Insert(node('E'),-1)
    print('\n---Test to insert "E" at end:')
    print(link)
    print('**Length**: ', link.len())


if __name__ == '__main__':
    test()
