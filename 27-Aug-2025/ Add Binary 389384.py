# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        t = int(a, 2) + int(b, 2)
        return bin(t)[2:]