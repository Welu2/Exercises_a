# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels={"a","e","i","o","u"}
        def is_vowel_word(word):
            return word[0] in vowels and word[-1] in vowels

        
        n = len(words)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if is_vowel_word(words[i]) else 0)

      
        result = []
        for li, ri in queries:
            result.append(prefix[ri + 1] - prefix[li])

        return result