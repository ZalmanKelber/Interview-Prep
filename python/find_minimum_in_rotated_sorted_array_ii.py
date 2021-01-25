class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            #if the left pointer is pointing to a smaller number, than the right pointer, we're done
            if nums[l] < nums[r]:
                return nums[l]
            #otherwise, find the midpoint
            med = l + (r - l) // 2
            #if the midpoint is higher than the left pointer, move the left pointer past it
            if nums[med] > nums[l] or (nums[med] == nums[l] and nums[l] > nums[r]):
                l = med + 1
            elif nums[med] < nums[l]:
                r = med
            #if the left pointer, mid pointer and right pointer all have the same value, we don't know where the higher
            #or lower values are and must increment the left pointer one at a time
            else:
                l += 1
        return nums[l]