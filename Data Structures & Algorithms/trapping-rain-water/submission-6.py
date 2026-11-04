class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0] * len(height)
        suf = [0] * len(height)
        i = 1
        while i < len(height):
            pre[i] = max(height[i-1], pre[i-1])
            i += 1
        i = len(height) - 2
        while i >= 0:
            suf[i] = max(height[i+1], suf[i+1])
            i -= 1
        res = 0
        for i in range(len(height)):
            water = max(min(pre[i], suf[i]) - height[i], 0)
            res += water
        return res