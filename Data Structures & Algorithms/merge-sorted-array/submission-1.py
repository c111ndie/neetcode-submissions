class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
    
        if not nums2:
            return
        elif not nums1:
            nums1 = nums2.copy()
            return
        
        p1 = p2 = 0
        l1 = m
        while p1 < m and p2 < n:
            if nums1[p1] > nums2[p2]:
                nums1[p1 + 1 : l1 + n] = nums1[p1 : l1 + n - 1] 
                nums1[p1] = nums2[p2]
                p1 += 1
                p2 += 1
                m += 1
            else:
                p1 += 1
        if p2 < n:
            nums1[m : l1 + n] = nums2[p2 : ]
            
        