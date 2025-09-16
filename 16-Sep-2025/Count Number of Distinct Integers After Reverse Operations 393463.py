# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def rev(num):
            s = str(num)
            if len(s)==1: return int(num)
            ans = []
            for j in range(len(s)-1, -1, -1):
                ans.append(s[j])
            return int("".join(ans))
        for i in range(len(nums)):
            nums.append(rev(nums[i]))
        c = Counter(nums)
        return len(c)