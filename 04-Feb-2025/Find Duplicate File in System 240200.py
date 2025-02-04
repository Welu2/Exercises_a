# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for path in paths:
            part=path.split(" ")
            directory=part[0]
            for j in part[1:]:
                name,data=j.split("(")
                
                result[data].append(f"{directory}/{name}")
        answer=[]
        
        for j in result:
            if len(result[j]) >1:
                answer.append(result[j])

        return answer