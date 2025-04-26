# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)

        
        for a, b in richer:
            graph[b].append(a)

        answer = [-1] * n

        def dfs(person):
            if answer[person] != -1:
                return answer[person]

          
            min_quiet = person

            for richer_person in graph[person]:
                candidate = dfs(richer_person)
                if quiet[candidate] < quiet[min_quiet]:
                    min_quiet = candidate

            answer[person] = min_quiet
            return min_quiet

        for i in range(n):
            dfs(i)

        return answer