class Solution:
    def countArrangement(self, n: int) -> int:
        self.n = n
        self.unused_nums = set([i for i in range(1, n + 1)])
        self.stack = []
        self.num_solutions = 0
        self.backtrack()
        return self.num_solutions
        
    def backtrack(self) -> None:
        index = len(self.stack)
        if index == self.n:
            self.num_solutions += 1
            return
        for num in self.unused_nums.copy():
            if num % (index + 1) == 0 or (index + 1) % num == 0:
                self.stack.append(num)
                self.unused_nums.remove(num)
                self.backtrack()
                self.unused_nums.add(self.stack.pop())