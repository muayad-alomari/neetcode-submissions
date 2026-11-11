class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        Xor = len(nums)

        for i in range(len(nums)):
            Xor ^=i^nums[i]
        return Xor    
    