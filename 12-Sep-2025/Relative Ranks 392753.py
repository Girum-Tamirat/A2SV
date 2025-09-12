# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ss = sorted(enumerate(score), key = lambda x:-x[1])
        meds = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ans = [""]*len(score)
        for rank, (i, sc) in enumerate(ss, start=1):
            if rank<=3:
                ans[i] = meds[rank-1]
            else:
                ans[i] = str(rank)
        return ans