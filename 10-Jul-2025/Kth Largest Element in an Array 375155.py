# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        bucket = []
        for num in nums:
            heapq.heappush(bucket, num)
            if len(bucket)>k:
                heapq.heappop(bucket)
        return bucket[0]