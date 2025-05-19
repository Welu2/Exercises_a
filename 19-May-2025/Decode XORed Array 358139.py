# Problem: Decode XORed Array - https://leetcode.com/problems/decode-xored-array/description/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        a=[first]
        
        for i in range(len(encoded)):
            a.append(encoded[i]^a[i])

        return a

        