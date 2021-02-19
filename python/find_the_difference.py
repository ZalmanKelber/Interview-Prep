class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sol = 0
        for ch in s:
            sol ^= ord(ch)
        for ch in t:
            sol ^= ord(ch)
        return chr(sol)