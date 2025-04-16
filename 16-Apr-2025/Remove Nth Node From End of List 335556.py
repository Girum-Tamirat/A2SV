# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        current = head
        while current:
            c += 1
            current = current.next
        if c == n:
            return head.next
        current = head
        for _ in range(c - n - 1):
            current = current.next
        current.next = current.next.next
        return head