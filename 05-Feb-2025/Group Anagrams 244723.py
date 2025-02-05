# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        anagram=[]
        for i in strs:
            s=sorted(i)
            a[tuple(s)].append(i)
        
        for j in a.values():
            anagram.append(j)

        return anagram
