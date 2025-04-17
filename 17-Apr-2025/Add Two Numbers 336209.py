# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lsta = []
        lstb = []
        #reverse
        def rev(self, head):
            prev, cur = None, head
            while cur is not None:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            return prev
        #join and map and sum and finally split as list to int them
        a = rev(self,l1)
        b = rev(self,l2)
        while a:
            lsta.append(a.val)
            a = a.next
        while b:
            lstb.append(b.val)
            b = b.next
        x = int("".join(map(str, lsta)))
        y = int("".join(map(str, lstb)))
        z = x + y
        lst = list(map(int, str(z)))
        lst.reverse()
        #then add them to a new linked list
        dummy = ListNode(0)
        cur = dummy
        for digit in lst:
            cur.next = ListNode(digit)
            cur = cur.next
        return dummy.next
