class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sol = 0
        for num in nums:
            sol ^= num
        return sol