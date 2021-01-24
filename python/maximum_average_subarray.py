class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #get the first average
        first_k_sum = 0
        for i in range(k):
            first_k_sum += nums[i]
        cur_average = first_k_sum / k
        max_average = cur_average
        for i in range(k, len(nums)):
            #get the new average by removing the first element and adding newest
            cur_average = cur_average - nums[i - k] / k + nums[i] / k
            max_average = max(cur_average, max_average)
        return max_average