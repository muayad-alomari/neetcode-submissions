class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        colors = [0] * 3
        for num in nums:
            colors[num] +=1
        r,w,b = colors[0], colors[1],colors[2]
        nums[0:r] = [0]*r
        nums[r:w+r] = [1] * w
        nums[w+r:] = [2] * b
        return nums
           
