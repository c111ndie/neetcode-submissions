class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = defaultdict(list)
        cnt = 0
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node):
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor not in visit:
                    dfs(neighbor)
            return
        for node in range(n):
            if node not in visit:
                dfs(node)
                cnt += 1
                if len(visit) == n:
                    return cnt
        
        