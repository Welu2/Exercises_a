# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a=''
        b=''
        for i in word1:
            a+=i
        for j in word2:
            b+=j

        return a == b