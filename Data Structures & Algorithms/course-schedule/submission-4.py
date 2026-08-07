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
        completed = 0
        q = deque()
        for c in range(numCourses):
            if pre_cnt[c] == 0: 
                completed += 1
                q.append(c) 
        while q and completed < numCourses:
            pre = q.popleft()
            for c in p_map.get(pre, []):
                if pre_cnt[c] > 0:
                    pre_cnt[c] -= 1
                    if pre_cnt[c] == 0:
                        completed += 1
                        q.append(c)
        return True if completed == numCourses else False



            
        