"""
class Solution:
    #use merge sort with recursion
    def sortArray(self, nums: List[int]) -> List[int]:
        #if this is a recursive base case, we don't need to do anything
        if len(nums) > 1:
            #divide list into sub problems, solve them and then merge them
            left = self.sortArray(nums[:len(nums) // 2])
            right = self.sortArray(nums[len(nums) // 2:])
            ptr1, ptr2 = 0, 0
            for i in range(len(nums)):
                if ptr1 == len(left) or (ptr2 < len(right) and right[ptr2] < left[ptr1]):
                    nums[i] = right[ptr2]
                    ptr2 += 1
                else:
                    nums[i] = left[ptr1]
                    ptr1 += 1
        return nums
"""

class Solution:
    #faster solution relies on limitation of integer range
    def sortArray(self, nums: List[int]) -> List[int]:
        values = defaultdict(int)
        largest, smallest = nums[0], nums[0]
        for num in nums:
            values[num] += 1
            largest = max(largest, num)
            smallest = min(smallest, num)
        ptr = 0
        for i in range(smallest, largest + 1):
            for j in range(values[i]):
                nums[ptr] = i
                ptr += 1
        return nums