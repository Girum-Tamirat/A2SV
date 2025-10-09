# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = []
        for i in address:
            if i != ".":
                a.append(i)
            else:
                a.append("[")
                a.append(i)
                a.append("]")
        return "".join(a)