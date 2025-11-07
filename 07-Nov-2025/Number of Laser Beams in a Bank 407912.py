# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        total = 0
        for row in bank:
            curr = row.count('1')
            if curr:
                total += prev * curr
                prev = curr
        return total