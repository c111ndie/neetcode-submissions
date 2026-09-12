class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2
        ans = 0
        if (m + n) % 2 == 1:
            l, r = 0, 0
            for _ in range(mid + 1):
                if nums1[l:] and nums2[r:] and nums1[l] < nums2[r]:
                    ans = nums1[l]
                    l += 1
                elif nums1 and nums2 and nums1[l] > nums2[r]:
                    ans = nums2[r]
                    r += 1
                elif nums1:
                    ans = nums1[l]
                    l += 1
                else:
                    ans = nums2[r]
                    r += 1
        else:
            l, r = 0, 0
            for _ in range(mid):
                if nums1[l:] and nums2[r:] and nums1[l] < nums2[r]:
                    ans = nums1[l]
                    l += 1
                elif nums1[l:] and nums2[r:] and nums1[l] > nums2[r]:
                    ans = nums2[r]
                    r += 1
                elif nums1[l:]:
                    ans = nums1[l]
                    l += 1
                else:
                    ans = nums2[r]
                    r += 1
            if nums1[l:] and nums2[r:]:
                ans = (ans + min(nums1[l], nums2[r])) / 2
            elif nums1[l:]:
                ans = (ans + nums1[l]) / 2
            else:
                ans = (ans + nums2[r]) / 2
        return ans
        