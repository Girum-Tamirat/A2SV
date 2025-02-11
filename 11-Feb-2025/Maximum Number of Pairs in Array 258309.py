# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        answer = []
        pairs = 0
        leftovers = 0
        n = Counter(nums)
        for i in n.values():
            pairs += i // 2
            leftovers += i % 2
        answer.append(pairs)
        answer.append(leftovers)
        return answer

