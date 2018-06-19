#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:27:24 2018

@author: xingyichong
"""
# linked list

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
       
class linkedlist:
    def __init__(self, iter=None):
        self.head = None
        if iter:            # Enable Factory Function
            for x in iter:
                self.insert(node(x))
     
    @property
    def length(self):
        curnode = self.head
        l = 0
        while curnode:
            l += 1
            curnode = curnode.next
        return l
      
    @property
    def tail(self):
        return self._index(self.length - 1)
    
    @property
    def isempty(self):
        return self.head == None


    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        curnode = self.head
        while curnode:
            yield curnode.data
            curnode = curnode.next
            
    def __getitem__(self, index):
        return self._index(index).data
    
    def __eq__(self, other):
        if self.length == other.length:
            for a, b in zip(self, other):
                return a == b
        else:
            return False
                    
       

    def insert(self, newNode, index=-1):
        """ Insert a node at a given position
         index = -1: insert at the end. (Default)
         index = 0: insert at the head
         index > 0: insert after this position 
         * note the first element index is 1 rather than 0 """
        
        try:
            if index < -1:
                index = self.length + index
            
            if self.isempty:
                self.head = newNode
                return
            
            if index == 0:
                newNode.next = self.head
                self.head = newNode
                
            elif index == -1:
                self.tail.next = newNode
            else:
                curnode = self._index(index - 1)
                nextnode = curnode.next
                
                curnode.next = newNode
                newNode.next = nextnode
                
        except (ValueError, IndexError) as err:
            print(err)
        
    
    def _index(self, index):
        if index < 0:
            index = self.length + index
        
        if index > self.length - 1 or index < 0:
            raise IndexError
        
        i = 0
        curnode = self.head
        while i < index:
            i += 1
            curnode = curnode.next
        return curnode
    

    def __str__(self):
        if self.isempty:
            strforprint = 'Empty LinkedList'
        else:
            strforprint = 'Below, the linked list:' + '\n================\n'
            curnode = self.head
            while curnode:
                strforprint += str(curnode.data)
                strforprint += '\n'
                curnode = curnode.next
        return strforprint
    