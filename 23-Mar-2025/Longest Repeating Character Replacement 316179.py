# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, ans,= 0, 0
        f = defaultdict(int)
        for j in range(len(s)):
            f[s[j]] += 1
            mx = max(f.values())
            c = j - i + 1
            if c - mx > k:
                f[s[i]] -= 1
                i += 1
            ans = max(ans, j-i+1)
        return ans