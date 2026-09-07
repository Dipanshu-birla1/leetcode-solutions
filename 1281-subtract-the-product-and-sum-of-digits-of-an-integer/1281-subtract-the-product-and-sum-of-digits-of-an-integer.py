class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n 
        sum = 0
        multi = 1
        while temp>0:
            r=temp%10
            temp//=10
            sum+=r
            multi*=r
        return (multi - sum)    


