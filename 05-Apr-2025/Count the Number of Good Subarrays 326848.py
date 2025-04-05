# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = i = 0
        c = Counter()
        for j in range(len(nums)):
            k -= c[nums[j]]
            c[nums[j]] += 1
            while k <= 0:
                c[nums[i]] -= 1
                k += c[nums[i]]
                i += 1
            ans += i
        return ans