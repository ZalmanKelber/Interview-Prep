class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = { len(s): True }
        def backtrack(index: int) -> bool:
            if index not in memo:
                for word in wordDict:
                    if s.find(word, index) == index:
                        if backtrack(index + len(word)):
                            memo[index] = True
                            break
                if index not in memo:
                    memo[index] = False
            return memo[index]
        return backtrack(0)