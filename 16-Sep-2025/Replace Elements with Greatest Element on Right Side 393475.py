# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mr = -1
        for i in range(n-1, -1, -1):
            arr[i], mr = mr, max(mr, arr[i])
        return arr