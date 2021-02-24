def gcf(k: int, n: int) -> int:
    for i in range(k, 0, -1):
        if k / i == k // i and n / i == n // i:
            return i

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0: return
        iterations = gcf(k, len(nums))
        for i in range(iterations):
            ptr = i
            cont = True
            val = nums[ptr]
            while cont:
                ptr += k
                ptr %= len(nums)
                new_val = nums[ptr]
                nums[ptr] = val
                val = new_val
                if ptr == i:
                    cont = False