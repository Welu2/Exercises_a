# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        a=[]
        for i in range(len(score)):
            a.append([score[i][k],score[i]])
        
        a.sort(reverse=True)
        b=[]
        for i in range(len(a)):
            b.append(a[i][1])

        return b