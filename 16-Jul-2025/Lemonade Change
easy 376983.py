# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiv = ten = 0
        for bill in bills:
            if bill == 5:
                fiv+=1
            elif bill == 10:
                if fiv > 0:
                    fiv-=1
                    ten+=1
                else:
                    return False
            else:
                if fiv>0 and ten>0:
                    fiv-=1
                    ten-=1
                elif fiv>2:
                    fiv=fiv-3
                else:
                    return False
        return True