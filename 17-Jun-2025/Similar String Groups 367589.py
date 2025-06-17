# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def are_similar(a, b):
            if a == b:
                return True
            diff = [(x, y) for x, y in zip(a, b) if x != y]
            return len(diff) == 2 and diff[0] == diff[1][::-1]

        def dfs(node, visited):
            visited.add(node)
            for nei in range(len(strs)):
                if nei not in visited and are_similar(strs[node], strs[nei]):
                    dfs(nei, visited)

        visited = set()
        groups = 0
        for i in range(len(strs)):
            if i not in visited:
                dfs(i, visited)
                groups += 1
        return groups