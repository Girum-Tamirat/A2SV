# Problem: Extra Characters in a String - https://leetcode.com/problems/extra-characters-in-a-string/description/

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            for j in range(i + 1, n + 1):
                if s[i:j] in word_set:
                    dp[i] = min(dp[i], dp[j])
        return dp[0]