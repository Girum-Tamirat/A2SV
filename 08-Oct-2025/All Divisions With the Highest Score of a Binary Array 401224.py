# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total_ones = sum(nums)
        left_zeros = 0
        right_ones = total_ones
        max_score = -1
        result = []

        for i in range(len(nums) + 1):
            score = left_zeros + right_ones
            if score > max_score:
                max_score = score
                result = [i]
            elif score == max_score:
                result.append(i)

            if i < len(nums):
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1

        return result