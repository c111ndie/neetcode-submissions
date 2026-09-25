class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        def connected(node, target, visit):
            if node == target:
                return True
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor not in visit:
                    if connected(neighbor, target, visit):
                        return True
            return False
        for a, b in edges:
            if connected(a, b, set()):
                return [a, b]
            adj[a].append(b)
            adj[b].append(a)