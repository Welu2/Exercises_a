# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq_matrix = [[False] * numCourses for _ in range(numCourses)]
       
        graph = [[] for _ in range(numCourses)]
       
        indegree = [0] * numCourses
      
       
        for course, next_course in prerequisites:
            graph[course].append(next_course)
            indegree[next_course] += 1
     
        queue = deque([i for i, count in enumerate(indegree) if count == 0])
      
        
        while queue:
            current_course = queue.popleft()
            for next_course in graph[current_course]:
               
                prereq_matrix[current_course][next_course] = True
              
                for course in range(numCourses):
                    prereq_matrix[course][next_course] = prereq_matrix[course][next_course] or prereq_matrix[course][current_course]
               
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
      
        return [prereq_matrix[start_course][end_course] for start_course, end_course in queries]