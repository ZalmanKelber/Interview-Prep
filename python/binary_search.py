class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        #start each pointer at the ends of the list and modify until there are no
        #values in between them
        while l < r:
            med = l + (r - l) // 2
            if nums[med] == target: 
                return med
            if nums[med] > target:
                r = med - 1
            else:
                l = med + 1
        #check if the final values of r and l find the target
        if l < len(nums) and nums[l] == target:
            return l
        if r >= 0 and nums[r] == target:
            return r
        return -1