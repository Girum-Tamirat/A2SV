# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j, chemistry = 0, len(skill)-1, 0
        sm = skill[i] + skill[j]
        while i < j:
            if skill[i] + skill[j] != sm:
                return -1
            chemistry += skill[i] * skill[j]
            i += 1
            j -= 1
        return chemistry