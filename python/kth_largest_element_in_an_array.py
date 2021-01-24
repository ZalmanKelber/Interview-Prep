import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #store the first k elements in a heap
        q = [nums[i] for i in range(k)]
        heapq.heapify(q)
        #add each new element to the heap and then pop and element from the heap 
        #so that the holds the k smallest elements
        for i in range(k, len(nums)):
            heapq.heappush(q, nums[i])
            heapq.heappop(q)
        #the largest of the k smallest elements will be the kth largest element
        return q[0]