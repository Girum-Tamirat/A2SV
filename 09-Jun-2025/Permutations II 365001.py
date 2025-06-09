# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(comb, count):
            if len(comb) == len(nums):
                res.append(list(comb))
                return
            for num in count:
                if count[num] > 0:
                    comb.append(num)
                    count[num] -= 1
                    backtrack(comb, count)
                    comb.pop()
                    count[num] += 1
        backtrack([], Counter(nums))
        return res