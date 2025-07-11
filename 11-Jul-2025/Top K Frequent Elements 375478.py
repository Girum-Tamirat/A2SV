# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        for num, freq in c.items():
            heappush(heap, (freq, num))
            if len(heap)>k:
                heappop(heap)
        return [num for freq, num in heap]
