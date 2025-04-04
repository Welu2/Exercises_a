# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result=[]
        if len(s) < 4 or len(s) > 12:
            return result
        def is_valid(segment) -> bool:
            return 0 <= int(segment) <= 255 and (segment == "0" or segment[0] != "0")
            return 0 <= int(s[start: end + 1]) <= 255
        for i in range(1, min(len(s), 4)):      
            for j in range(i + 1, min(len(s), i + 4)):  
                for k in range(j + 1, min(len(s), j + 4)):  
                
                    part1, part2, part3, part4 = s[:i], s[i:j], s[j:k], s[k:]
                    
                
                    if is_valid(part1) and is_valid(part2) and is_valid(part3) and is_valid(part4):
                        
                        result.append(f"{part1}.{part2}.{part3}.{part4}")
        
        return result

     
      