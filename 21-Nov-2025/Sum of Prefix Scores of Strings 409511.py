# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        
        # Insert words into the Trie
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                node.count += 1
        
        # Compute answer for each word
        ans = []
        for w in words:
            node = root
            total = 0
            for c in w:
                node = node.children[c]
                total += node.count
            ans.append(total)
        
        return ans