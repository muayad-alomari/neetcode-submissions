class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        perm = []
        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for x in nums:
                if x not in perm:
                    perm.append(x)
                    dfs()
                    perm.pop()
        dfs()
        return res                
        