# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        a = [int(d) for d in str(abs(num)) ]
        nz = [num for num in a if num != 0]
        ans = []
        if num > 0:
            mn = min(nz)
            ans.append(mn)
            a.sort()
            a.remove(mn)
            for i in a:
                ans.append(i)
        elif num < 0:
            mx = max(nz)
            a.sort(reverse=True)
            a.remove(mx)
            ans.append('-')
            ans.append(mx)
            for i in a:
                ans.append(i)
        else:
            return 0
        if ans[0] == '-':
            return -int("".join(map(str, ans[1:])))
        return int("".join(map(str, ans)))