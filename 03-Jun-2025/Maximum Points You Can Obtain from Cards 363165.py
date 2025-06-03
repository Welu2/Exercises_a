# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_pts=sum(cardPoints)
        n=len(cardPoints)
        cur=sum(cardPoints[:n-k])
        ans=total_pts-cur
        for i in range(n-k,n):
            cur-=cardPoints[i-(n-k)]
            cur+=cardPoints[i]


            ans=max(ans,total_pts-cur)

        return ans
