class Solution:
    def checkValidString(self, s: str) -> bool:
        if not len(s): return True
        #keep track of star_indices in a deque, so that we can add them and remove the first ones when necessary
        star_indices = deque()
        #will keep track of the 'parentheses depth' (number of open parentheses subtracted by number of close parentheses) for each index of the string
        paren_depths = []
        current_depth = 0
        for i, ch in enumerate(s):
            if ch == "*": star_indices.append(i)
            else: current_depth += 1 if ch == "(" else -1
            #if current depth is negative, convert the LEFTMOST remaining star into an open parenthesis.  If none exists, the string isn't valid: return False
            if current_depth < 0:
                if len(star_indices) < 1:
                    return False 
                else:
                    new_open_paren_index = star_indices.popleft()
                    #update the paren_depths and current_depth to take into account the added open parenthesis
                    for j in range(new_open_paren_index, len(paren_depths)):
                        paren_depths[j] += 1
                    current_depth += 1
            paren_depths.append(current_depth)
        #if the last parentheses depth isn't 0, we have a deficit of close parentheses.
        #find the RIGHTMOST remaining star and convert it into a close parenthesis, and check that this doesn't cause any new negative parentheses depths when updates
        while paren_depths[-1] != 0:
            if len(star_indices) < 1: return False 
            new_close_paren_index = star_indices.pop()
            for j in range(new_close_paren_index, len(paren_depths)):
                if paren_depths[j] == 0: return False
                paren_depths[j] -= 1
        return True