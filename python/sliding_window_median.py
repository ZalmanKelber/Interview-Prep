"""
#slow solution:
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
"""

import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        #if k equals 1, each element in nums is its own window and own median
        if k == 1:
            return nums
        #keep track of median with two heaps
        lower_heap, upper_heap = [], [nums[0]]
        median = nums[0]
        median_list = []
        for i in range(1, len(nums)):
            #remove the first element of the previous window when necessary
            if i >= k:
                to_remove = nums[i - k]
                if to_remove >= median:
                    upper_heap.remove(to_remove)
                    heapq.heapify(upper_heap)
                else:
                    lower_heap.remove(to_remove * -1)
                    heapq.heapify(lower_heap)
            #add the next element 
            num = nums[i]
            if num >= median:
                heapq.heappush(upper_heap, num)
            else:
                heapq.heappush(lower_heap, num * -1)
            #balance heaps and get the median.  If this is a window (that is, if i is greater or equal to k - 1), add it to the median list
            median = self.balance_heaps(lower_heap, upper_heap)
            if i >= k - 1: 
                median_list.append(median)
        return median_list
        
        
    def balance_heaps(self, lower_heap: List[int], upper_heap: List[int]) -> float:
        while len(lower_heap) > len(upper_heap):
            heapq.heappush(upper_heap, heapq.heappop(lower_heap) * -1)
        while len(upper_heap) > len(lower_heap) + 1:
            heapq.heappush(lower_heap, heapq.heappop(upper_heap) * -1)
        return upper_heap[0] if len(upper_heap) > len(lower_heap) else (upper_heap[0] + lower_heap[0] * -1) / 2