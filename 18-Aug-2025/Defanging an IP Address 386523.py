# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=""
        for i in address:
            if i =='.':
                s+='[.]'
            else:
                s+=i

        return s