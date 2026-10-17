
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {value: i for i, value in enumerate(nums)}

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or pos[arr[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[arr[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
