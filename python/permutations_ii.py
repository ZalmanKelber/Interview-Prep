class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # track the progress outside of the recursive flow
        self.nums = nums
        self.solutions = set()
        self.stack = []
        self.unused_indices = set([i for i in range(len(nums))])
        self.backtrack()
        return [list(sol) for sol in self.solutions]
    
    def backtrack(self) -> None:
        #recursive base case: if stack is complete, add it as a tuple to solutions set to prevent duplicates
        if len(self.unused_indices) == 0:
            self.solutions.add(tuple(self.stack))
        else:
            #add each possible next number and call the backtracking function
            for i in self.unused_indices.copy():
                self.stack.append(self.nums[i])
                self.unused_indices.remove(i)
                self.backtrack()
                self.unused_indices.add(i)
                self.stack.pop()