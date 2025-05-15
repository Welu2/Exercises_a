# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = defaultdict(int)
        count[0] = 1  
        mask = 0
        result = 0

        for ch in word:
            bit = ord(ch) - ord('a')
            mask ^= (1 << bit)  
            
            result += count[mask]

            
            for i in range(10):  
                result += count[mask ^ (1 << i)]

          
            count[mask] += 1

        return result