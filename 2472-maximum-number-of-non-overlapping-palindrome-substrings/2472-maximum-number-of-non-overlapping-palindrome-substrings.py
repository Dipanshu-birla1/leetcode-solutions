class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n):
            dp[i + 1] = max(dp[i + 1], dp[i])

            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)
                    break
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)
                    break
                l -= 1
                r += 1

        return dp[n]