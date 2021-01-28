class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        solution = []
        found = set()
        for num in nums:
            if num in found:
                solution.append(num)
            else:
                found.add(num)
        return solution