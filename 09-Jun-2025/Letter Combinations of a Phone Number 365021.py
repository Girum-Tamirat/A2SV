# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if not digits:
                return []
        pm = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backtrack(i, cur):
            if i == len(digits):
                ans.append(cur)
                return
            for letter in pm[digits[i]]:
                backtrack(i + 1, cur + letter)
        backtrack(0, "")
        return ans