# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.Children = [None for _ in range(26)]  
        self.is_end = False 
class Trie:
    

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            num = ord(char) - 97
            if curr.Children[num] is None:
                curr.Children[num] = TrieNode()
            curr = curr.Children[num]
        curr.is_end = True
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            num = ord(char) - 97
            if curr.Children[num] is None: 
                return False
            curr = curr.Children[num]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            num = ord(char) - 97
            if curr.Children[num] is None:
                return False
            curr = curr.Children[num]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)