class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            r = num % k
            new_dp = [0] * k

            new_dp[r] += 1

            for rem in range(k):
                if dp[rem]:
                    new_rem = (rem * r) % k
                    new_dp[new_rem] += dp[rem]

            dp = new_dp

            for rem in range(k):
                result[rem] += dp[rem]

        return result