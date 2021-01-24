class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #keep track of how many of each character is in each substring
        num_chars = { "a": 0, "b": 0, "c": 0 }
        start_index, end_index = 0, -1
        total_substrings = 0
        while end_index < len(s):
            #increment end_index until substring is valid
            while not self.containsAbc(num_chars) and end_index < len(s):
                end_index += 1
                if end_index < len(s):
                    num_chars[s[end_index]] += 1
            #if there are no valid substrings for the given start index, exit the while loop
            if end_index >= len(s):
                break
            #add the number of substrings with the given start index and end index greater or equal to end_index
            total_substrings += len(s) - end_index
            num_chars[s[start_index]] -= 1
            start_index += 1
        return total_substrings
        
    def containsAbc(self, num_chars: dict) -> bool:
        if num_chars["a"] == 0 or num_chars["b"] == 0 or num_chars["c"] == 0:
            return False
        return True