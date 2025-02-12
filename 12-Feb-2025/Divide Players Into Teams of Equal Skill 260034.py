# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=0
        r=len(skill)-1
        d=defaultdict(list)
        total=0
        while l < r:
            d[skill[l]+skill[r]].append([skill[l],skill[r]])
            total+=(skill[l]*skill[r])
            l+=1
            r-=1

        if len(d) >1:
            return -1
        return total
        