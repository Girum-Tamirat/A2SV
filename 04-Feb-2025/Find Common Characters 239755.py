# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        
        freq = Counter(words[0])        
        for word in words[1:]:
            current_freq = Counter(word)
            for char in freq:
                if char in current_freq:
                    freq[char] = min(freq[char], current_freq[char])
                else:
                    freq[char] = 0
        
        result = []
        for char, count in freq.items():
            result.extend([char] * count)
        
        return result