# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c=Counter(deck)
        freq=set()
        
        for j in c:
            freq.add(c[j])
        
        result = reduce(gcd, freq)
        if result > 1:
            return True

        return False
        