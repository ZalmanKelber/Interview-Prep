class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        #traverse the string and keep track of the paren_depth – the number of open parens subtracted by the number of close parens
        paren_depth = 0
        #store the characters that aren't removed in a list to allow for constant time insertion
        chars_to_retain = []
        for ch in S:
            #use paren_depth to determine whether or not a character is an outer-layer parenthesis
            if (paren_depth != 0 or ch != "(") and (paren_depth != 1 or ch != ")"):
                chars_to_retain.append(ch)
            paren_depth += 1 if ch == "(" else -1
        return "".join(chars_to_retain)

#problem: https://leetcode.com/problems/remove-outermost-parentheses