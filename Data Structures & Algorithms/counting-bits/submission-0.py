class Solution:
    def countBits(self, n: int) -> List[int]:


        myl = []

        for i in range(n+1):
            one = 0
            for j in range(32):
                lDigit = i&1
                if lDigit :
                    one +=1
                i = i>>1
            myl.append(one)
            
        return myl            