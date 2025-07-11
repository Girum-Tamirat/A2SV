# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        mh = [-pile for pile in piles]
        heapify(mh)
        for _ in range(k):
            l = -heappop(mh)
            q = ceil(l/2)
            heappush(mh, -q)
        return -sum(mh)