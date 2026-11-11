class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mydic = defaultdict(int)

        for i in arr :
            mydic[i] +=1

        mymax = -1
        for k,v in mydic.items():
            if mymax<mydic[k] and k==v:
                mymax = mydic[k]
        return mymax              
        