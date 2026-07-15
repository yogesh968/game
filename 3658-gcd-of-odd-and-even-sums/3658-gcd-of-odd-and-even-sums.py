import math 
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        summOfOdd  = 0 
        summOfeven  = 0 
        for i in range(1,n*2+1):
            if i %2==0:
                summOfeven+=i
        for i in range(1,n*2+1):
            if i%2==1:
                summOfOdd+=i
        GCD = math.gcd(summOfOdd,summOfeven)
        return GCD
        