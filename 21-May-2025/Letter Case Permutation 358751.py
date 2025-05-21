# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = [i for i, c in enumerate(s) if c.isalpha()]
        n = len(letters)
        res = []

        for bits in range(1 << n):  
            chars = list(s)
            for i in range(n):
                idx = letters[i]
                if (bits >> i) & 1:
                    chars[idx] = chars[idx].upper()
                else:
                    chars[idx] = chars[idx].lower()
            res.append("".join(chars))
        
        return res