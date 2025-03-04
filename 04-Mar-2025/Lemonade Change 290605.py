# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=Counter()
        for i in bills:
            if i == 5:
                a[i]+=1
            elif i == 10:
                if a[5] > 0:
                    a[i]+=1
                    a[5]-=1
                else:
                    return False
            else:
                if a[10] > 0 and a[5] > 0:
                    a[10]-=1
                    a[5]-=1

                elif a[5] >= 3:
                    a[5]-=3
                else:
                    return False
                    


    
        
        return True