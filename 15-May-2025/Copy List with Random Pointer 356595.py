# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
    
        curr = head
        while curr:
            copied = Node(curr.val)
            copied.next = curr.next
            curr.next = copied
            curr = copied.next
        
        curr = head
        while curr:
            copied = curr.next
            if curr.random:
                copied.random = curr.random.next
            curr = copied.next
        
        dummy = Node(0)
        copied_curr = dummy
        curr = head
        
        while curr:
            copied_curr.next = curr.next
            copied_curr = copied_curr.next
            
            curr.next = copied_curr.next
            curr = curr.next
        
        return dummy.next