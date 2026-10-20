m = 100001
div = [[] for _ in range(m)]
for i in range(2, m):
    for j in range(i, m, i):
        div[j].append(i)

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        right = [n]*n 
        for i in range(n-2,-1,-1):
            if nums[i] > nums[i + 1]:
                right[i] = i
            else:
                right[i] = right[i + 1] 
        a = 0
        if right[0] == n: a = 1 
        def f(k):
            pre = 0
            for r in range(k - 1, n, k):
                l = r - k + 1
                m = right[l]
                if m > r:
                    if nums[l] < pre:
                        return 
                    pre = nums[r]
        
                else:
                    if right[m + 1] < r or nums[m + 1] < pre or nums[r] > nums[l]:
                        return 
                    pre = nums[m]
            nonlocal a 
            a += k
        for d in div[n]:
            f(d)
        return a         