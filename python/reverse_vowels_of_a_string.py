"""
#slower solution: 
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = { "a", "e", "i", "o", "u" }
        #keep track of vowels we find, in order
        vowel_stack = []
        #keep track of string indices that have vowels, in order
        vowel_indices = []
        #store the result as a list since strings are not mutable
        result = [None for i in range(len(s))]
        for i, ch in enumerate(s):
            if ch.lower() in vowels:
                vowel_stack.append(ch)
                vowel_indices.append(i)
            else:
                #if the character isn't a vowel, we can add it in its current index to the result
                result[i] = ch
        for i in vowel_indices:
            result[i] = vowel_stack.pop()
        return "".join(result)
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = { "a", "e", "i", "o", "u" }
        # use a list since its mutable
        s_as_list = list(s)
        left_pointer, right_pointer = -1, len(s)
        # the left and right pointers search for vowels one at a time and switch them
        while right_pointer > left_pointer:
            left_pointer += 1
            while left_pointer < len(s) and s_as_list[left_pointer].lower() not in vowels:
                left_pointer += 1
            right_pointer -= 1
            while right_pointer >= 0 and s_as_list[right_pointer].lower() not in vowels:
                right_pointer -= 1
            if right_pointer > left_pointer:
                s_as_list[left_pointer], s_as_list[right_pointer] = s_as_list[right_pointer], s_as_list[left_pointer]
        return "".join(s_as_list)