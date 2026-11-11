class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
       
        if endWord not in wordList or endWord == beginWord:
            return 0
        g = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                g[pattern].append(word)
        
        q = deque()
        visit = set()
        q.append(beginWord)
        visit.add(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:] 
                    for nei in g[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            res +=1        
        return 0

