class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        mid = (m + n) // 2
        l, r = 0, m 
        while l <= r:
            i = (l + r) // 2
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            left2 = nums2[mid - i - 1] if mid - i > 0 else float("-inf")
            right1 = nums1[i] if i < len(nums1) else float("inf")
            right2 = nums2[mid - i] if mid - i < len(nums2) else float("inf")
            if left1 > right2:
                r = i - 1
            elif left2 > right1:
                l = i + 1
            else:
                right_min = min(right1, right2)
                if (m + n) % 2:
                    return right_min
                left_max = max(left1, left2)
                return (left_max + right_min) / 2
