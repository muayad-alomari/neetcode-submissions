class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        

        if s_len != t_len :
            return False

        countS , countT = defaultdict(int),defaultdict(int)
        for i in  range(len(s)):
         countS[s[i]] +=1
         countT[t[i]] +=1
        return countS==countT



