class Solution:
    def binaryGap(self, n: int) -> int:
        biggest_gap = 0
        last_1 = None
        index = 0
        while n:
            if n & 1:
                if last_1 is not None:
                    biggest_gap = max(biggest_gap, index - last_1)
                last_1 = index
            index += 1
            n = n>>1
        return biggest_gap