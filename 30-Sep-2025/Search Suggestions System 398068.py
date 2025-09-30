# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.suggestions = []
class Solution:
    def buildTrie(self, products: List[str]) -> TrieNode:
        root = TrieNode()
        for product in sorted(products): 
            node = root
            for char in product:
                node = node.children[char]
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)
        return root
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = self.buildTrie(products)
        result = []
        node = root

        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                node = None
                result.append([])
        return result