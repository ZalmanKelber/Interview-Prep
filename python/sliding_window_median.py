class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = nums[:k]
        window.sort()
        medians = []
        for i in range(k, len(nums) + 1):
            if k % 2 == 1:
                medians.append(window[k // 2])
            else:
                medians.append(window[k // 2] / 2 + window[k // 2 - 1] / 2)
            if i < len(nums):
                self.shift_sorted_window(window, nums[i - k], nums[i])
        return medians
    
    def shift_sorted_window(self, window: List[int], to_remove: int, to_insert: int) -> None:
        index_to_remove = window.index(to_remove)
        for i in range(index_to_remove, len(window) - 1):
            window[i] = window[i + 1]
        index_to_insert = 0
        while window[index_to_insert] < to_insert and index_to_insert < len(window) - 1:
            index_to_insert += 1
        for i in range(len(window) - 1, index_to_insert, -1):
            window[i] = window[i - 1]
        window[index_to_insert] = to_insert