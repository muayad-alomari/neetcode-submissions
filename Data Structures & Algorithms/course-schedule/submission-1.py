class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if g[crs] == []:
                return True 

            visiting.add(crs)
            for i in g[crs]:
                if not dfs(i):
                    return False
            visiting.remove(crs)  
            g[crs] =[]       
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True    

