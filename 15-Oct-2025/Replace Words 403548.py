# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
           # Step 1: Build the Trie
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

        # Step 2: Define function to find the root replacement
        def find_root(word):
            node = root
            prefix = ""
            for char in word:
                if char not in node.children:
                    return word  # no matching root
                node = node.children[char]
                prefix += char
                if node.is_end:
                    return prefix  # found shortest root
            return word  # no root found

        # Step 3: Process sentence
        return " ".join(find_root(word) for word in sentence.split())