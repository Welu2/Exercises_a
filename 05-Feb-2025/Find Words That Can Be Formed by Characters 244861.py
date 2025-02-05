# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total=0
        freqChars=Counter(chars)
        for i in words:
            freqWord=Counter(i)
            if all(freqChars[j]>=freqWord[j] for j in freqWord):
                total+=len(i)

        return total