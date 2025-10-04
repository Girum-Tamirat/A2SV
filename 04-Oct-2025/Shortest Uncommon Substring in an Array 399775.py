# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        substring_to_indices = defaultdict(set)
        for i, word in enumerate(arr):
            seen = set()
            for start in range(len(word)):
                for end in range(start + 1, len(word) + 1):
                    substr = word[start:end]
                    if substr not in seen:
                        substring_to_indices[substr].add(i)
                        seen.add(substr)
        result = []
        for i, word in enumerate(arr):
            candidates = []
            for start in range(len(word)):
                for end in range(start + 1, len(word) + 1):
                    substr = word[start:end]
                    if substring_to_indices[substr] == {i}:  
                        candidates.append(substr)
            if candidates:
                candidates.sort(key=lambda x: (len(x), x))
                result.append(candidates[0])
            else:
                result.append("")
        return result