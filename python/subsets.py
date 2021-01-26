class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #store the stack and solutions outside of the recursion flow
        self.stack = []
        self.solutions = []
        self.nums = nums
        self.backtrack(0)
        return self.solutions
    
    def backtrack(self, index: int) -> None:
        #if we've gone through all of nums, add the present stack to the solutions list
        if index == len(self.nums):
            self.solutions.append(self.stack[:])
            return
        #otherwise, increment index and call the backtracking function with both the next number added or not added
        self.backtrack(index + 1)
        self.stack.append(self.nums[index])
        self.backtrack(index + 1)
        self.stack.pop()