class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g  = defaultdict(list)
        q = collections.deque()
        inorder = [0] * numCourses
        for a,b in prerequisites:
            g[b].append(a)
            inorder[a] +=1

        for i in range(numCourses):
            if inorder[i] == 0 :
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in g[node]:
                inorder[nei] -=1
                if inorder[nei] == 0:
                    q.append(nei)
        if len(res) != numCourses:
            return []
        return res                           
        