class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        five_remainder = 0
        result = []
        for num in A:
            five_remainder *= 2
            five_remainder += num
            five_remainder %= 5
            result.append(True if five_remainder == 0 else False)
        return result