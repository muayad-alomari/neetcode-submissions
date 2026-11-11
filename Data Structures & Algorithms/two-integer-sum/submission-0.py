class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i,n in enumerate(nums) :
            indices[n] = i

        
        for i,n in enumerate(nums):
            differ = target - n
            if differ in indices and indices [differ] !=i:
               return [i , indices[differ]]
        return[]    
      