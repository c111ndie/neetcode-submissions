class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = set()
        p_map = {}
        pre_cnt = [0] * numCourses
        for c, pre in prerequisites:
            if pre not in p_map:
                p_map[pre] = [c]
            else:
                p_map[pre].append(c)
            pre_cnt[c] += 1

        q = deque()
        for c in range(numCourses):
            if pre_cnt[c] == 0: 
                taken.add(c)
                q.append(c) 
        while q and len(taken) < numCourses:
            pre = q.popleft()
            for c in p_map.get(pre, []):
                if c not in taken:
                    pre_cnt[c] -= 1
                    if pre_cnt[c] == 0:
                        taken.add(c)
                        q.append(c)
        if len(taken) == numCourses:
            return True
        return False



            
        