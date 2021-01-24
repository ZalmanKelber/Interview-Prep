class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #ptr1 will traverse nums1 in reverse.  ptr2 will traverse nums2 in reverse
        ptr1, ptr2 = m - 1, n - 1
        #i traverses the full nums1 in reverse, adding the final elements
        for i in range(m + n - 1, -1, -1):
            if ptr1 < 0 or (ptr2 >= 0 and nums2[ptr2] > nums1[ptr1]):
                nums1[i] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1