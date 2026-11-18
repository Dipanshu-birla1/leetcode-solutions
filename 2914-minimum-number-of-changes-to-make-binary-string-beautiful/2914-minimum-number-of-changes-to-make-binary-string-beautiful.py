class Solution:
    def minChanges(self, s: str) -> int:
        

        return sum([1 if s[i] != s[i+1] else 0 for i in range(0, len(s), 2)])
