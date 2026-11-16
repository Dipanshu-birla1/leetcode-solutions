
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            result = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]
                total = sum(int(digit) for digit in group)
                result += str(total)

            s = result

        return s
