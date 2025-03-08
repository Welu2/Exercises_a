# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = current_depth = 0
  
        for index, char in enumerate(s):
            if char == '(':  
                current_depth += 1  
            else:  
                current_depth -= 1  
                if s[index - 1] == '(':
                    score += 1 << current_depth
        return score