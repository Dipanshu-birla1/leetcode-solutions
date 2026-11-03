
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)

        moves = 0

        for num in nums:
            moves += maximum - num

        return moves
