from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = deque()
        sw = deque()
        for i in range(len(students)):
            s.append(students[i])
            sw.append(sandwiches[i])
        no_streak = 0
        while no_streak < len(sw):
            if s[0] == sw[0]:
                s.popleft()
                sw.popleft()
                no_streak = 0
            elif s[0] != sw[0]:
                s.append(s[0])
                s.popleft()
                no_streak += 1
        return len(s)