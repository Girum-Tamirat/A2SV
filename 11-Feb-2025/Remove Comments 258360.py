# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        res = []
        buffer = ""
        
        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if i + 1 < len(line) and line[i:i+2] == "*/":
                        in_block = False
                        i += 1
                elif i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 1
                elif i + 1 < len(line) and line[i:i+2] == "//":
                    break 
                else:
                    buffer += line[i]
                i += 1
            
            if not in_block and buffer:
                res.append(buffer)
                buffer = ""
        
        return res
                