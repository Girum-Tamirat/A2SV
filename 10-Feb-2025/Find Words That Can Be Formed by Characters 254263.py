# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ca = Counter(chars)
        tot = 0
        
        for word in words:
            cb = Counter(word)
            if all(cb[i] <= ca[i] for i in cb):
                tot += len(word)
        
        return tot