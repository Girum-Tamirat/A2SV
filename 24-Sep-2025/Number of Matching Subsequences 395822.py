# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                node = node.children[ch]
            node.count += 1  
        def dfs(node: TrieNode, index: int) -> int:
            total = node.count
            for ch, child in node.children.items():
                next_idx = s.find(ch, index)
                if next_idx != -1:
                    total += dfs(child, next_idx + 1)
            return total

        return dfs(root, 0)