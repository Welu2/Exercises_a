# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result=[]
        for i in words:
            lowerCase=i.lower()
            if all(j in "asdfghjkl" for j in set(lowerCase)):
                result.append(i)
            elif all(j in "zxcvbnm" for j in set(lowerCase)):
                result.append(i)
            elif all(j in "qwertyuiop" for j in set(lowerCase)):
                result.append(i)

        return result

