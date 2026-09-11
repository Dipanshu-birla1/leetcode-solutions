class Solution:
    def totalNumbers(self, digits):
        count = [0] * 10

        
        for d in digits:
            count[d] += 1

        ans = 0

       
        for first in range(1, 10):
            if count[first] == 0:
                continue

            count[first] -= 1

         
            for second in range(10):
                if count[second] == 0:
                    continue

                count[second] -= 1

              
                for last in range(0, 10, 2):
                    if count[last] > 0:
                        ans += 1

                count[second] += 1

            count[first] += 1

        return ans