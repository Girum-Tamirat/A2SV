# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mst = {}
        mts = {}
        for cs, ct in zip(s,t):
            if (cs in mst and mst[cs] != ct) or (ct in mts and mts[ct] != cs):
                return False
            mst[cs] = ct
            mts[ct] = cs
        return True