# Problem: Freedom Trail - https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
    
    # Step 1: Map each character to all its indices in ring
        char_to_indices = defaultdict(list)
        for i, ch in enumerate(ring):
            char_to_indices[ch].append(i)

        # Step 2: Min-heap for Dijkstra-style BFS: (total_steps, ring_pos, key_pos)
        heap = [(0, 0, 0)]
        visited = dict()  # (ring_pos, key_pos): min_steps

        while heap:
            steps, ring_pos, key_pos = heapq.heappop(heap)

            if key_pos == len(key):
                return steps  # Finished spelling

            if (ring_pos, key_pos) in visited and visited[(ring_pos, key_pos)] <= steps:
                continue  # Already visited with fewer steps

            visited[(ring_pos, key_pos)] = steps
            target_char = key[key_pos]

            for target_pos in char_to_indices[target_char]:
                diff = abs(ring_pos - target_pos)
                step_cost = min(diff, ring_len - diff) + 1  # +1 for pressing center
                heapq.heappush(heap, (steps + step_cost, target_pos, key_pos + 1))

        return -1  # Guaranteed solvable by constraints