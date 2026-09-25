class Solution:
    def dfs(self, src, adj, visit, path, topSort):
        if src in path:
            return False
        if src in visit:
            return True
        visit.add(src)
        path.add(src)
        if src in adj:
            for neighbor in adj[src]:
                if not self.dfs(neighbor, adj, visit, path, topSort):
                    return False
        topSort.append(src)
        path.remove(src)
        return True


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {}
        for c, pre in prerequisites:
            if c not in adj:
                adj[c] = [pre]
            else:
                adj[c].append(pre)
        topSort = []
        path = set()
        visit = set()
        
        for i in range(numCourses):
            if not self.dfs(i, adj, visit, path, topSort):
                return []
        return topSort
            
        
        

        