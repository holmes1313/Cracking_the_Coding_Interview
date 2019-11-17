# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 23:17:04 2019

@author: z.chen7
"""


# 2. Linked Lists
"""
A linked lists is a data structure that represents a sequence of nodes.
In a single linked list, each node points to the next node in the linked lists.

The benefit of a linked list is that you can add and remove items from 
the beginning of the list in constant time.

# the runner technique (two pointers)
You could have one pointer fast move every two steps for every one move that
slow moves. When fast hits the end of the linked list, slow will be at the midpoint.

Delting a node form a singly linked list
Given a node n, we find the previous node prev and set prev.next equal to n.next.
The important thinkgs to remember are
    (1) to check for the null pointer
    (2) to update the head or tail pointer as necessary.
"""
def deleteNode(head, d):
    if not head:
        return None
    
    curr = head
    
    if curr.val == d:
        return head.next
    
    while curr.next:
        if curr.next.val == d:
            curr.next = curr.next.next
        curr = curr.next
    return head


# interview questions

# 2.7 intersection
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curr1 = headA
        curr2 = headB
        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA
