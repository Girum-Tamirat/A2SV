# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        w = s[::-1].split()
        w.sort()
        r = [i[1:][::-1] for i in w]
        return " ".join(r)