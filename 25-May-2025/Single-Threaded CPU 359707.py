# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
    
        result = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:
            while i < n and indexed_tasks[i][0] <= time:
                enqueue_time, processing_time, index = indexed_tasks[i]
                heapq.heappush(heap, (processing_time, index))
                i += 1
            
            if heap:
                proc_time, idx = heapq.heappop(heap)
                time += proc_time
                result.append(idx)
            else:
                time = indexed_tasks[i][0]
        
        return result