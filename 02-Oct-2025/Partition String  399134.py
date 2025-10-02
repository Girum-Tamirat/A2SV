# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        curr = ""
        for c in s:
            curr += c
            if curr in seen:
                continue
            else:
                res.append(curr)
                seen.add(curr)
                curr = ""
        return res