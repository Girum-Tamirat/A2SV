# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        evs = sum(num for num in nums if num% 2 == 0 )

        for v, i in queries:
            oldv = nums[i]
            if oldv % 2 == 0:
                evs -= oldv
            nums[i] += v
            if nums[i] % 2 == 0:
                evs += nums[i]
            answer.append(evs)
        return answer