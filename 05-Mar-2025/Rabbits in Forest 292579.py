# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter=Counter(answers)
        min_no_rabbits=0
        for i in counter:
            if counter[i] == 1 or i+1 >=  counter[i]:
                min_no_rabbits+=i+1
            else:
                value=counter[i]//(i+1)
                if counter[i] % (i+1) != 0:
                    min_no_rabbits+=(i+1)*(value+1)
                else:
                    min_no_rabbits+=(i+1)*(value)




       
        return min_no_rabbits
       