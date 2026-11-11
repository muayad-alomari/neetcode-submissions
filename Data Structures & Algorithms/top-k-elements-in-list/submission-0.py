class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

       
            count = Counter(nums)
            bucket = [0] * (len(nums) + 1)

            for num, freq in count.items():
                if bucket[freq] == 0:
                    bucket[freq] = [num]
                else:
                    bucket[freq].append(num)

            res = []
            for i in range(len(bucket)-1, -1, -1):
                    if bucket[i] != 0:
                        res.extend(bucket[i])
                    if len(res) == k:  
                            break   
            return res



        