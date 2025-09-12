# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [0]*len(score)
        for i in range(1, len(score)+1):
            a = score.index(max(score))
            ans[a] = str(i)
            score[a] = -1
        ans[ans.index('1')] = "Gold Medal"
        if len(ans) >= 2: ans[ans.index('2')] = "Silver Medal"
        if len(ans) >= 3: ans[ans.index('3')] =  "Bronze Medal"
        return ans