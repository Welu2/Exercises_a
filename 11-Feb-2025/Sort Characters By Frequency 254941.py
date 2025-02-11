# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        a=''
        b=Counter(s)
        c= b.most_common()
        for i,j in c:
            o= i *j
            a+=o

        return a
