class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)
        visited = set()
        res = []
        def dfs(crs, cycle):
            if crs in cycle:
                return False
            cycle.add(crs)
            for pre in preMap[crs]:
                if pre not in visited:
                    if not dfs(pre, cycle):
                        return False
            res.append(crs)
            visited.add(crs)
            return True
        for n in range(numCourses):
            if n not in visited:
                cycle = set()
                if not dfs(n, cycle):
                    return []
        return res
        