# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
    
        def flatten_helper(node):
            curr = node
            while curr:
                if curr.child:
                    child_head = curr.child
                    child_tail = flatten_helper(child_head)
                    
                    next_node = curr.next
                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None
                    
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail
                    
                    curr = next_node if next_node else child_tail
                else:
                    curr = curr.next
            
            tail = node
            while tail and tail.next:
                tail = tail.next
            return tail
        
        flatten_helper(head)
        return head