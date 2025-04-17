# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        temp, n = head, 0
        while temp.next:
            n += 1
            temp = temp.next
        k %= n+1
        last = temp
        if k == 0:
            return head
        nt = head
        for _ in range(n - k):
            nt = nt.next
        nh = nt.next
        nt.next =  None
        last.next = head
        return nh