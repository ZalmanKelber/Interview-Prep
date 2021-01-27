class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #keep track of progress outside of the recursion flow
        self.nums = nums
        self.solutions = []
        self.unused_indices = set([i for i in range(len(nums))])
        self.stack = []
        self.backtrack()
        return self.solutions
    
    def backtrack(self) -> None:
        #recursion base case: if stack is complete, add it to solutions
        if len(self.unused_indices) == 0:
            self.solutions.append(self.stack[:])
            return
        #for each unused index, add the next corresponding value of nums to the stack before calling backtrack again
        for i in self.unused_indices.copy():
            self.stack.append(self.nums[i])
            self.unused_indices.remove(i)
            self.backtrack()
            self.unused_indices.add(i)
            self.stack.pop()