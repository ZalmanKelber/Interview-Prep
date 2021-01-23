class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        num_needed = 0 #keeps track of number of parentheses necessary to make the string valid; added to for each string segment
        num_open_parens = 0 #keeps track of number of open parentheses in the current segment
        num_close_parens = 0
        for i, ch in enumerate(S):
            if ch == "(": num_open_parens += 1
            else: num_close_parens += 1
            #if there are more close parentheses than open parentheses, end the current segment, add the difference to num_needed, and refresh the two counters
            if ch == ")" and num_close_parens > num_open_parens: 
                num_needed += num_close_parens - num_open_parens
                num_open_parens, num_close_parens = 0, 0
        num_needed += num_open_parens - num_close_parens
        return num_needed