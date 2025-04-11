# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j, c = 0, len(people)-1, 0
        while i <= j:
            if i < j and people[i] + people[j] <= limit:
                i += 1
                j -= 1
                c += 1
            else:
                j -= 1
                c += 1
        return c