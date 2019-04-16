
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        if n1 == 0:
            if n2 % 2 == 1:
                return nums2[n2/2]
            return (nums2[(n2 - 1) / 2] + nums2[n2 / 2]) * 0.5
                
        
        k = (n1 + n2 + 1) / 2
        
        l, r = 0, n1
        
        while l < r:
            m1 = (l + r) / 2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                l = m1 + 1
            else:
                r = m1
        m1 = l
        m2 = k-l
        
        
        c1 = max(-float('inf') if m1 <= 0 else nums1[m1-1],
                -float('inf') if m2 <= 0 else nums2[m2-1])
        
        if (n1 + n2) % 2 == 1:
            return c1
        
        c2 = min(float('inf') if m1 >= n1 else nums1[m1],
                float('inf') if m2 >= n2 else nums2[m2])
        
        return (c1 + c2) * 0.5
        
        
