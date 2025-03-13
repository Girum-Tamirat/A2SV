# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        i = 0
        while i < len(chars):
            c = 1
            j = i + 1
            while j < len(chars) and chars[i] == chars[j]:
                c += 1
                j += 1
            s.append(chars[i])
            if c > 1:
                s.extend(list(str(c)))
            i = j
        chars.clear()
        chars.extend(s)
        return len(chars)