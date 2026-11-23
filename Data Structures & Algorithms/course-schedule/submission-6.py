class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p_to_c = {}
        for c, p in prerequisites:
            if p not in p_to_c:
                p_to_c[p] = []
            p_to_c[p].append(c)
        def dfs(p, path):
            nonlocal p_to_c
            if p in path:
                return False
            path.add(p)
            if p in p_to_c:
                for c in p_to_c[p]:
                    if not dfs(c, path):
                        return False
            path.remove(p)
            p_to_c[p] = [] 
            return True
        for crs in range(numCourses):
            if not dfs(crs, set()):
                return False
        return True
