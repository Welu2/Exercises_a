# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
      
        def perm(path,open,close):
        
            if len(path) == 2*n:
                ans.append("".join(path))
                return 
            if open < n:
                path.append("(")
                perm(path,open+1,close)
                path.pop()
            if close < open:
                path.append(")")
                perm(path,open,close+1)
                path.pop()



            
        perm([],0,0)
        return ans
                