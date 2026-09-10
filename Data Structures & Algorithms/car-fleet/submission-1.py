class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for pos, spd in pair:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
    
        return len(stack)