class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n = len(position)
        for i in range(n):
            stack.append((position[i], speed[i]))
        stack.sort(reverse=True)
        times = []
        for pos, spd in stack:
            t = (target - pos) / spd
            if not times or t > times[-1]:
                times.append(t)
        return len(times)
            