# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        tot = 0
        y = 0
        for char in reversed(s):
            v = roman_values[char]
            if v < y:
                tot -= v
            else:
                tot += v
            y = v
        return tot
