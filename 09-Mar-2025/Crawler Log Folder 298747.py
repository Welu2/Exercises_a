# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
       
        folder_level = 0
      
       
        for operation in logs:
            if operation == "../":
                folder_level = max(0, folder_level - 1)
            elif operation != "./":
                
                folder_level += 1
      
      
        return folder_level