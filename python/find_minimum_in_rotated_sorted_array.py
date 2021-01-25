class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        #in the final result, l will point to the minimum and r will be greater or equal to l
        while nums[l] > nums[r]:
            med = l + (r - l) // 2
            if nums[med] >= nums[l]:
                l = med + 1
            else:
                r = med
        return nums[l]