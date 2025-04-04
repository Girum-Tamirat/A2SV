# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m, m+n):
            if nums1[i] == 0:
                nums2.sort()
                nums1[i] = nums2[j]
                j += 1
        nums1.sort()