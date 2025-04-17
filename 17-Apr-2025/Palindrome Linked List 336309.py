# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        c = 0
        left = right = temp = head
        while temp:
            c += 1
            temp = temp.next
        c //= 2
        for _ in range(c):
            left = left.next
        def rev(head):
            prev, cur = None, head
            while cur:
                nn = cur.next
                cur.next = prev
                prev = cur
                cur = nn
            return prev
        right = rev(left)
        left = head
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True