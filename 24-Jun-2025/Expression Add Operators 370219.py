# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []
        def dfs(pos, exp):
            if pos==n:
                if eval(exp)==target:
                    ans.append(exp)
                return
            for i in range(pos+1, n+1):
                if len(num[pos:i])>1 and num[pos:i][0]=="0":
                    continue
                if pos==0:
                    dfs(i, num[pos:i])
                else:
                    dfs(i, exp + "+" + num[pos:i])
                    dfs(i, exp + "-" + num[pos:i])
                    dfs(i, exp + "*" + num[pos:i])
            return
        dfs(0, "")
        return ans