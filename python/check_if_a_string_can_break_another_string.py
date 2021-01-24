"""
#slower solution
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ascii_values1 = [0 for i in range(26)]
        ascii_values2 = [0 for i in range(26)]
        for ch in s1:
            ascii_values1[ord(ch) - 97] += 1
        for ch in s2:
            ascii_values2[ord(ch) - 97] += 1
        nums1, nums2 = [], []
        for i in range(len(ascii_values1)):
            for j in range(ascii_values1[i]):
                nums1.append(i)
            for j in range(ascii_values2[i]):
                nums2.append(i)
        s1_breaks_s2, s2_breaks_s1 = True, True
        for i in range(len(nums1)):
            if nums1[i] > nums2[i]:
                s1_breaks_s2 = False
            if nums2[i] > nums1[i]:
                s2_breaks_s1 = False
            if not s1_breaks_s2 and not s2_breaks_s1:
                return False
        return True
"""
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        #sort strings (since we only need to iterate through them, there's no need to join them back into strings)
        ss1, ss2 = sorted(s1), sorted(s2)
        s1_breaks_s2, s2_breaks_s1 = True, True
        #iterate through sorted strings to determine if one breaks the other
        for i in range(len(s1)):
            if ord(ss1[i]) > ord(ss2[i]):
                s2_breaks_s1 = False
            if ord(ss2[i]) > ord(ss1[i]):
                s1_breaks_s2 = False
            if not s1_breaks_s2 and not s2_breaks_s1:
                return False
        return True