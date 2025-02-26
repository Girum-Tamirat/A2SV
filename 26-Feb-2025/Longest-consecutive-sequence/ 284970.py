# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        l = 0
        for num in d:
            if num - 1 not in d:
                c = num
                s = 1
                while c + 1 in d:
                    c += 1
                    s +=1
                l = max(l, s)
        return l
