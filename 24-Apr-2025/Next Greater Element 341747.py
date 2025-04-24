# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stc = []
        res = defaultdict(lambda: -1)
        for num in nums2:
            while stc and stc[-1] < num:
                res[stc.pop()] = num
            stc.append(num)
        return [res[num] for num in nums1]