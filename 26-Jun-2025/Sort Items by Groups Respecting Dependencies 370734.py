# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1

        # Step 2: Build graphs and in-degree maps
        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(list)
        group_indegree = [0] * new_group_id

        # Group to items mapping
        group_to_items = defaultdict(list)
        for i in range(n):
            group_to_items[group[i]].append(i)

        for curr in range(n):
            for prev in beforeItems[curr]:
                # Item graph
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                # Group graph
                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        # Topological sort helper
        def topological_sort(graph, indegree, nodes):
            res = []
            queue = deque([node for node in nodes if indegree[node] == 0])
            while queue:
                node = queue.popleft()
                res.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            return res if len(res) == len(nodes) else []

        # Step 3: Topo sort groups
        all_groups = list(range(new_group_id))
        sorted_groups = topological_sort(group_graph, group_indegree, all_groups)
        if not sorted_groups:
            return []

        # Step 4: Topo sort items within each group
        result = []
        for grp in sorted_groups:
            items = group_to_items[grp]
            if not items:
                continue
            sub_graph = defaultdict(list)
            sub_indegree = {i: 0 for i in items}
            for i in items:
                for nei in item_graph[i]:
                    if nei in sub_indegree:
                        sub_graph[i].append(nei)
                        sub_indegree[nei] += 1
            sorted_items = topological_sort(sub_graph, sub_indegree, items)
            if not sorted_items:
                return []
            result.extend(sorted_items)

        return result
            