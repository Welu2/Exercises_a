# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.d=defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.d[key]=val
        node=self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def sum(self, prefix: str) -> int:
        # total=0
        # for char in d:
        #     if char not in node.children:
        #        total+= node.children[char]
        # return total 
        def dfs(node, path):
            total = 0
            full_key = ''.join(path)
            if node.is_end:
                total += self.d[full_key]
            for char, child in node.children.items():
                total += dfs(child, path + [char])
            return total

        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return dfs(node, list(prefix))

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)