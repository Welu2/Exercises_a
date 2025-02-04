# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letter=[]
        while columnNumber > 0:
                columnNumber-=1
                letter.append(chr((columnNumber%26)+65))
                columnNumber//=26
        return "".join(letter[::-1])

       