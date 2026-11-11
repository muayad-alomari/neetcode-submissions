class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n 

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            else: return x 

        def union(a, b):
            r, l = find(a), find(b)
            if r == l:
                return 0 
            if rank[r] < rank[l]:
                r , l = l, r
            parent[l] = r
            if  rank[r] == rank[l]:  
                rank[r] += 1
            return 1 
        res = n    
        for a, b in edges:
            res -= union(a,b)
        return res    




