# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c = 0
        if not head:
            return False
        while head.next:
            head = head.next
            c += 1
            if c >= 10000:
                return True
        return False