class Solution:
    def climbStairs(self, n: int) -> int:
        
        first_pointer = 1
        second_pointer = 1
        for i in range(n-1):
            temp = first_pointer
            first_pointer = first_pointer +second_pointer
            second_pointer = temp
        return first_pointer    
            

