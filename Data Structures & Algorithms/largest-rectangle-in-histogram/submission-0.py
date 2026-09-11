class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            forward = i
            while stack and stack[-1][1] > heights[i]:
                forward = stack[-1][0]
                max_area = max(max_area, (i - stack[-1][0]) * stack[-1][1])
                stack.pop()
            stack.append((forward, heights[i]))
        for i in range(len(stack)):
            max_area = max(max_area, (len(heights) - stack[i][0]) * stack[i][1])
        return max_area