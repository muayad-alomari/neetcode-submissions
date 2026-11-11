class Solution:
    def hammingWeight(self, n: int) -> int:

        c = 0
        while n :
            lastDigit = n&1
            n = n>>1
            if lastDigit ==1 :
                c +=1
        return c        
        