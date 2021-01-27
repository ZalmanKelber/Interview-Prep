class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.stack = []
        self.cur_sum = 0
        self.solutions = set()
        self.target = target
        self.candidates = candidates
        self.backtrack()
        return [list(sol) for sol in self.solutions]
    
    def backtrack(self) -> None:
        if self.cur_sum == self.target:
            self.solutions.add(tuple(self.stack))
            return
        for candidate in self.candidates:
            if self.cur_sum + candidate <= self.target and (len(self.stack) == 0 or candidate <= self.stack[-1]):
                self.stack.append(candidate)
                self.cur_sum += candidate
                self.backtrack()
                self.cur_sum -= candidate
                self.stack.pop()