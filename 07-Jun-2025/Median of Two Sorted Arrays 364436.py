# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1+nums2
        n.sort()
        if len(n)%2 != 0: 
            return n[len(n)//2]
        else: 
            return (n[len(n)//2-1]+n[(len(n)//2)])/2