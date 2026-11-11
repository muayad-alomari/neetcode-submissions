class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[r]:
                r = mid
            else :
                l = mid +1

        my_min = l
        l ,r = 0,len(nums)-1

        if target >= nums[my_min] and target <= nums[r]:
            l =my_min
        else :
            r = my_min-1    

        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l = m+1
            else :
                r = m-1
        return -1               


        