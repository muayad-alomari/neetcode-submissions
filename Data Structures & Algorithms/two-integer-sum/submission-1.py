class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i in range(len(nums)):
            indices[nums[i]] = i 
        
        for i in range(len(nums)):
            differ = target - nums[i]
            if differ in indices and indices [differ] !=i:
               return [i , indices[differ]]
        return[]    
      