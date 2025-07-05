# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num)):
            for j in range(i+1, len(num)):
                num1, num2 = num[:i], num[i:j]
                if (len(num1)>1 and num1[0]=="0") or (len(num2)>1 and num2[0]=="0"):
                    continue
                a, b= int(num1), int(num2)
                seq = num1+num2
                while len(seq)<len(num):
                    c = a+b
                    seq+=str(c)
                    a,b=b,c
                if seq==num: return True
        return False