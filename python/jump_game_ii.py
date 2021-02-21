class Solution:
    def jump(self, nums: List[int]) -> int:
        pos = 0
        num_jumps = 0
        while pos < len(nums) - 1:
            num_jumps += 1
            next_index = pos
            max_next_step = 0
            for i in range(1, nums[pos] + 1):
                if pos + i >= len(nums) - 1:
                    return num_jumps
                if i + nums[pos + i] > max_next_step:
                    max_next_step = i + nums[pos + i]
                    next_index = pos + i
            pos = next_index
                    
        return num_jumps