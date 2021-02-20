class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1: return False
        return bin(n).count("1") == 1 and bin(n).count("0") % 2 == 1