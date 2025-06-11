# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    res.append('.'.join(parts))
                return
            for l in range(1, 4):
                if start + l > len(s): break
                seg = s[start:start + l]
                if (seg.startswith('0') and len(seg) > 1) or int(seg) > 255:
                    continue
                backtrack(start + l, parts + [seg])
        backtrack(0, [])
        return res