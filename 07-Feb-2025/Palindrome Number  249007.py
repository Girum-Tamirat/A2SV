# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        orgx = x
        result = 0
        if x<0 or x%10==0 and x!=0:
            return False
        while x>0:
            digit=x%10
            result = result * 10 + digit
            x //= 10
            
        return orgx == result
