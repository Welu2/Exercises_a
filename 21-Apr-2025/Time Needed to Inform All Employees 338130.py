# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)
        for emp in range(n):
            if manager[emp] != -1:
                subordinates[manager[emp]].append(emp)

      
        def dfs(emp_id):
            if not subordinates[emp_id]:
                return 0
            max_time = 0
            for sub in subordinates[emp_id]:
                max_time = max(max_time, dfs(sub))
            return informTime[emp_id] + max_time

      
        return dfs(headID)