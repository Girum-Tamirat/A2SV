# Problem: Reorder List - https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stc = []
        cur = head
        while cur:
            stc.append(cur)
            cur = cur.next
        cur = head
        for _ in range(len(stc)//2):
            nxt = cur.next
            tl = stc.pop()
            cur.next = tl
            tl.next = nxt
            cur = nxt
        cur.next = None