class Solution:
    def reverse(self, x: int) -> int:
        Min = -2**31
        Max =  2**31 - 1
        if x>0:
            sign = 1
        else :
            sign = -1
        x = abs(x)        
        res = 0
        while x :
            d = x%10
            x //= 10
            if res >Max//10 or (res == Max//10 and d > Max%10):
                return 0
             

            res = res *10 + d
        return res*sign    
        