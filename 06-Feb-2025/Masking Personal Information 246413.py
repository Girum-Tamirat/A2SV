# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s = s.lower()
            name, domain = s.split("@")
            return name[0] + "*****" + name[-1] + "@" + domain
        else:
            digits = [c for c in s if c.isdigit()]
            local_number = "***-***-" + "".join(digits[-4:])
            if len(digits) > 10:
                return "+" + "*" * (len(digits) - 10) + "-" + local_number
            return local_number
