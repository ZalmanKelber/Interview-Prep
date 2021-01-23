"""
slow solution:

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not len(s): return 0
        paren_depth, min_depth, max_depth = 0, 0, 0
        starting_depths_to_indices = defaultdict(list)
        longest_lengths_by_starting_index = [0 for i in range(len(s))]
        for i, ch in enumerate(s):
            is_open = ch == "("
            if is_open:
                paren_depth += 1
                max_depth = max(paren_depth, max_depth)
                starting_depths_to_indices[paren_depth].append(i)
            else: 
                paren_depth -= 1
                min_depth = min(paren_depth, min_depth)
            for j in range(paren_depth + 2, max_depth + 1):
                starting_depths_to_indices[j] = []
            for index in starting_depths_to_indices[paren_depth + 1]:
                longest_lengths_by_starting_index[index] = i + 1 - index
        return max(longest_lengths_by_starting_index)
            
            
            
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #search for substrings where depth at start_index is one greater than depth at end_index - 1, 
        #and where no intermediate index has depth less than depth at end_index - 1
        starting_index = None
        starting_depth = None
        cur_depth = 0
        longest_found = 0
        for i, ch in enumerate(s):
            is_open = ch == "("
            cur_depth += 1 if is_open else -1
            #if starting index is None, start a new segment
            if is_open and starting_index is None:
                starting_index, starting_depth = i, cur_depth
            #if the present index satisfies the conditions for the end of a substring beginning with the current starting_index,
            #check if this substring is the longest found so far
            if ( not is_open and starting_depth is not None and 
                starting_depth - 1 == cur_depth ):
                longest_found = max(longest_found, i + 1 - starting_index)
                #if there are no possible valid substrings with the same start_index that end beyond this index, start a new segment
                #by setting starting_index and starting_depth to None 
                if i == len(s) - 1 or s[i + 1] == ")":
                    starting_index, starting_depth = None, None
        return max(longest_found, self.endingValidParentheses(s))
    
    #check from oposite direction
    def endingValidParentheses(self, s: str) -> int:
        #begin checking by locating the last close parentheses
        last_index = s.rfind(")")
        longest_found = 0
        cur_depth = 1
        for i in range(last_index - 1, -1, -1):
            cur_depth += 1 if s[i] == ")" else -1
            #if cur_depth is zero, this is a valid substring
            if cur_depth == 0:
                longest_found = max(longest_found, last_index + 1 - i)
                #if there are no valid substrings that include this substring, check the remaining portion of the string
                if i == 0 or s[i - 1] == "(":
                    return max(longest_found, self.endingValidParentheses(s[:i]))
        return longest_found