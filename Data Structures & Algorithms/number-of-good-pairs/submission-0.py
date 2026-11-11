class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        my_dict = defaultdict(int)

        for i in nums:

            my_dict[i] +=1
        res = 0
        for num, c in my_dict.items():
            res += c*(c-1)//2
        return res    
            