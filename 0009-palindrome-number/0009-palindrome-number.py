class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        a = []

        while temp > 0:
            r = temp % 10
            a.append(r)
            temp //= 10

        b = a[::-1]

        return a == b