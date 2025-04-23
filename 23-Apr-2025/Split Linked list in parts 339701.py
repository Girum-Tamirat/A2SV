# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        base_size, extra = divmod(length, k)
        
        result = []
        curr = head
        
        for i in range(k):
            part_head = curr
            
            size = base_size + (1 if extra > 0 else 0)
            
            for j in range(size - 1):
                if curr:
                    curr = curr.next
            
            if curr:
                next_start = curr.next
                curr.next = None
                curr = next_start
            else:
                curr = None
                
            result.append(part_head)
            if extra > 0:
                extra -= 1
        
        return result