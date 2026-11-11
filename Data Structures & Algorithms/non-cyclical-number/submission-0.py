class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()

        while n  not in visit:
            visit.add(n)
            n = self.sumOfSqueres(n)
            if n ==1:
                return True
        return False

    def sumOfSqueres(self,n):
            out = 0
            while n:
                d = n % 10
                d = d **2
                out += d 
                n = n//10
            return out        
        