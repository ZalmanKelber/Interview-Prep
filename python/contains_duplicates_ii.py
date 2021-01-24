class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #store last k values in a set for constant time lookup
        last_k_values = set()
        for i, num in enumerate(nums):
            #check if next value is in the last k values
            if num in last_k_values:
                return True
            #add the next value to the set
            last_k_values.add(num)
            #if necessary, remove the first value of the set
            if i >= k:
                last_k_values.remove(nums[i - k])
        return False