# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        c1, c2 = l1, l2
        while c1:
            s1 += str(c1.val)
            c1 = c1.next
        while c2:
            s2 += str(c2.val)
            c2 = c2.next
        a = int(s1) + int(s2)
        a = [int(d) for d in str(a)]
        res = ListNode(0)
        cur = res
        for i in a:
            cur.next = ListNode(i)
            cur = cur.next
        return res.next