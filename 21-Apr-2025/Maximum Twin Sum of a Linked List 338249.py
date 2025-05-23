# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        newList = None
        current = head
        currHalf = head
        while currHalf and currHalf.next:
            currHalf = currHalf.next.next
            temp = current.next
            current.next = newList
            newList = current
            current = temp
        while current:
            ans = max(ans, current.val + newList.val)
            current = current.next
            newList = newList.next
        return ans