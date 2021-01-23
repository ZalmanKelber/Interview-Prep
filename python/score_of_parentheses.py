class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        #recursion base caseL
        if len(S) <= 4: 
            return len(S) // 2
        #'segments' are the outer-layer substrings of parentheses (i.e. ones not enclosed within any other outler layer)
        segment_endpoints = [0]
        #depth is the number of open parentheses minus the number of close parentheses
        paren_depth = 0
        for i, ch in enumerate(S):
            paren_depth += 1 if ch == "(" else -1
            #if depth is zero, we've reached the end of a 'segment'
            if paren_depth == 0:
                segment_endpoints.append(i + 1)
        score = 0
        #add up the subscores of each segment
        for i in range(len(segment_endpoints) - 1):
            start_index = segment_endpoints[i] + 1
            end_index = segment_endpoints[i + 1] - 1
            if start_index == end_index:
                score += 1
            else:
                score += 2 * self.scoreOfParentheses(S[start_index:end_index])
        return score