class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()

        def dfs(parent,node):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if parent == nei:
                    continue
                if not dfs(node,nei):
                    return False    
            return True
        return dfs(-1,0) and len(visit) == n            



        