# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join(char.lower() for char in s if char.isalnum())
        i, j = 0, len(ss)-1
        ans = True
        while i < j:
            if ss[i] == ss[j]:
                i += 1
                j -= 1
                ans = True
            else:
                ans = False
                break
        return ans