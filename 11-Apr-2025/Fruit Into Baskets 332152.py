# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        b = {}
        i, mx = 0, 0
        for j in range(len(fruits)):
            b[fruits[j]] = b.get(fruits[j], 0) + 1
            while len(b) > 2:
                b[fruits[i]] -= 1
                if b[fruits[i]] == 0:
                    del(b[fruits[i]])
                i += 1
            mx = max(mx, j - i + 1)
        return mx