# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        num=["0",'1']
        def perm(path):
            nonlocal ans
            if len(path) == n:
                ans.append("".join(path))
                return 

            for i in num:
                if path and path[-1] == "0" and i == "0":
                    continue
                else:
                    path.append(i)
                    perm(path)
                    path.pop()

        perm([])
        return ans