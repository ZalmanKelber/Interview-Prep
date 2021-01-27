class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.unused_indices = set([i for i in range(len(candidates))])
        self.target = target
        self.solutions = []
        self.stack = []
        self.cur_sum = 0
        self.partials = set()
        self.backtrack()
        return [list(sol) for sol in self.solutions]
    
    def backtrack(self) -> None:
        if tuple(self.stack) in self.partials:
            return
        self.partials.add(tuple(self.stack))
        if self.cur_sum == self.target:
            self.solutions.append(self.stack[:])
            return
        for i in self.unused_indices.copy():
            candidate = self.candidates[i]
            if self.cur_sum + candidate <= self.target and (len(self.stack) == 0 or self.stack[-1] <= candidate):
                self.stack.append(candidate)
                self.cur_sum += candidate
                self.unused_indices.remove(i)
                self.backtrack()
                self.unused_indices.add(i)
                self.cur_sum -= candidate
                self.stack.pop()