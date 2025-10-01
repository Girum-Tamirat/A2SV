# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_end = True
    def find_root(self, word: str) -> str:
        node = self.root
        prefix = ''
        for ch in word:
            if ch not in node.children:
                return word  
            node = node.children[ch]
            prefix += ch
            if node.is_end:
                return prefix 
        return word  
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for root in dictionary:
            self.insert(root)

        words = sentence.split()
        replaced = [self.find_root(word) for word in words]
        return ' '.join(replaced)