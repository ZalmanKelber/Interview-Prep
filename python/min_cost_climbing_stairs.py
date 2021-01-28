class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.memo = { len(cost) - 1: cost[-1], len(cost) - 2: cost[-2] }
        self.cur_index = -1
        return self.backtrack()
    
    def backtrack(self) -> int:
        if self.cur_index not in self.memo:
            self.cur_index += 1
            left_sol = self.backtrack()
            self.cur_index += 1
            right_sol = self.backtrack()
            self.cur_index -= 2
            result = self.cost[self.cur_index] if self.cur_index >= 0 else 0
            result += min(left_sol, right_sol)
            self.memo[self.cur_index] = result
        return self.memo[self.cur_index]