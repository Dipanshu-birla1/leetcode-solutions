class Solution:
    def minInsertions(self, s: str) -> int:
        open = 0
        ans = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open += 1
                i += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2
                else:
                    ans += 1
                    i += 1

                if open > 0:
                    open -= 1
                else:
                    ans += 1

        return ans + 2 * open