class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #read pointer traverses list and to determine if element should be included in final list
        #write pointer adds values that are retained in the correct index
        read_pointer, write_pointer = 0, 0
        #penum and anti_penum track the previous two values to determine whether or not an element is a second duplicate
        penum, anti_penum = None, None
        while read_pointer < len(nums):
            #if the read element is not a duplicate, add it in the appropriate spot and increment the write pointer
            if nums[read_pointer] != anti_penum
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
            #update values
            anti_penum, penum, read_pointer = penum, nums[read_pointer], read_pointer + 1
        #remove excess list indices
        for i in range(len(nums) - write_pointer):
            nums.pop()
        return len(nums)