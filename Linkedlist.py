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
    def __init__(self, Iter=None):
        self.head = None
        if Iter:            # Enable Factory Function
            for x in Iter:
                self.insert(x)

    @property
    def length(self):
        curnode = self.head
        _len = 0
        while curnode:
            _len += 1
            curnode = curnode.next
        return _len

    @property
    def _tail(self):
        if not self.isempty:
            return self._index(-1)

    def tail(self):
        if not self.isempty:
            return self._tail.data

    @property
    def isempty(self):
        return self.head is None

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
        if self.length != other.length:
            return False

        for a, b in zip(self, other):
            if a != b:
                return False
        return True

    def insert(self, new, index=-1):
        """ Insert a node at a given position
         index = -1: insert at the end. (Default)
         index = 0: insert at the head
         otherwise: insert after this position
         * note the first element index is 1 rather than 0 """

        newNode = node(new)
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
                self._tail.next = newNode
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
        strforprint = ''
        for i in self:
            strforprint += str(i) + '\n'
        return strforprint
