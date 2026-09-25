class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visit = set()
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor != parent:
                    if not dfs(neighbor, node):
                        return False
            return True
        if not dfs(0, -1):
            return False
        return len(visit) == n
        