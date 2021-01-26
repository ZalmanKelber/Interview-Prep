numbers_to_letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #keep track of the solutions as well as the stack outside of the recursion flow
        self.solutions = []
        self.digits = digits
        #store partial solution as a list rather than a string to allow constant time appending and popping
        self.stack = []
        self.backtrack()
        return self.solutions
        
    def backtrack(self) -> None:
        #if the stack is full, add it to the list of solutions
        if len(self.stack) == len(self.digits):
            if len(self.stack) > 0:
                self.solutions.append("".join(self.stack))
            return
        #otherwise backtrack for each possible next character
        for ch in numbers_to_letters[self.digits[len(self.stack)]]:
            self.stack.append(ch)
            self.backtrack()
            self.stack.pop()