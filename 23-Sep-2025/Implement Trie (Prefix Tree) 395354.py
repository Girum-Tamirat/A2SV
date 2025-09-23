# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.children = [None]*26
        self.is_end = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                cur.children[i] = Trie()
            cur = cur.children[i]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return True       


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)