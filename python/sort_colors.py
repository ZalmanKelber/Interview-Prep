class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #store the count for each color
        colorCounts = [0 for i in range(3)]
        #traverse the list and read each subsequent color
        for i, color in enumerate(nums):
            #if the color is 0, add a 0 after the existing 0's
            #then, if there is at least one 1, add the removed 1 after the last existing 1
            if color == 0:
                nums[colorCounts[0]] = 0
                if colorCounts[1] > 0:
                    nums[colorCounts[0] + colorCounts[1]] = 1
            #if the color is 1, add a 1 after the last existing 1
            if color == 1:
                nums[colorCounts[0] + colorCounts[1]] = 1
            #if there is at least one 2, a 2 should be in the current position
            if colorCounts[2] > 0:
                nums[i] = 2
            colorCounts[color] += 1