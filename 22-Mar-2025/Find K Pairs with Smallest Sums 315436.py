# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        mh = []
        result = []
        for i in range(min(k, len(nums1))):
            heappush(mh, (nums1[i] + nums2[0], i, 0))
        while mh and len(result) < k:
            _, i, j = heappop(mh)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heappush(mh, (nums1[i] + nums2[j + 1], i, j + 1))
        return result