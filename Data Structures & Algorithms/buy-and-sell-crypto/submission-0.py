class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_ = 101
        max_ = -1

        for i in prices:
            if i<min_:
                min_=i
            p = i - min_
            max_ = max(p,max_)
        return max_                