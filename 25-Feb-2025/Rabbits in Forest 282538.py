# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = 0
        d = {}
        for ans in answers:
            if ans == 0:
                count += 1
            else:
                if ans not in d or ans == d[ans]:
                    d[ans] = 0
                    count += 1 + ans
                else:
                    d[ans] += 1
        return count