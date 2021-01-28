class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = {}
        for i, num in enumerate(nums):
            if target - num in indices_map:
                return [indices_map[target - num], i]
            indices_map[num] = i