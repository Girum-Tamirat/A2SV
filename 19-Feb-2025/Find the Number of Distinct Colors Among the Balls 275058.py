# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = [0] * len(queries)
        mp = {}
        color = defaultdict(int)
        i = 0

        for x, y in queries:
            if x in mp:
                y0 = mp[x]
                color[y0] -= 1
                if color[y0] == 0:
                    color.pop(y0)

            mp[x] = y
            color[y] += 1

            result[i] = len(color)
            i += 1
            
        return result