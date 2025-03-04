# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        if maxDoubles==0:
            return target-1
        else:
            
            while target > 1 :
                if target % 2 != 0:
                    target-=1
                    count+=1
                else:
                    target=target//2
                    maxDoubles-=1
                    count+=1

                if maxDoubles == 0:
                    break
        if target > 1:
            count+=target-1

        return count

                