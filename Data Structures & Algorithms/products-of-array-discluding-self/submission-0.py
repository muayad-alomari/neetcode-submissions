class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l = 1
        r = 1
        n = len(nums)
        right_arr = [0]*len(nums)
        left_arr = [0]*len(nums)

        for i in range(n):
            j = -i -1
            right_arr[i] = r
            r *=nums[i]
            left_arr[j] = l
            l *=nums[j]


        new_arr = [0]*n
        for i in range(n):
            new_arr[i] = right_arr[i]*left_arr[i]



        return new_arr    

            
            
         

        