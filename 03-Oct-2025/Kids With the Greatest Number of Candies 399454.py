# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        m = max(candies)
        for c in candies:
            if c + extraCandies >= m:
                result.append(True)
            else: 
                result.append(False)
        return result