'''
Amazon would like to know how much inventory exists in their closed inventory compartments. Given a string s
consisting of items as "*" and closed compartments as an open and close "|", an array of starting indices startIndices, and an array of ending indices endIndices, determine the number of items in closed compartments within the substring between the two indices, inclusive.

An item is represented as an asterisk ('*' = ascii decimal 42)
A compartment is represented as a pair of pipes that may or may not have items between them ('|' = ascii decimal 124). 
Example

s = '|**|*|*'

startIndices = [1, 1]

endIndices = [5, 6]

The string has a total of 2 closed compartments, one with 2 items and one with 1 item. For the first pair of indices, (1, 5), the substring is '|**|*'. There are 2 items in a compartment.

For the second pair of indices, (1, 6), the substring is '|**|*|' and there are 2 + 1 = 3 items in compartments.

Both of the answers are returned in an array, [2, 3].

Function Description

Complete the numberOfItems function in the editor below. The function must return an integer array that contains the results for each of the startIndices[i] and endIndices[i] pairs.

numberOfItems has three parameters:

s: A string to evaluate

startIndices: An integer array, the starting indices.

endIndices: An integer array, the ending indices. 

Constraints

1 ≤ m, n ≤ 10^5  ==> n is the length of n
1 ≤ startIndices[i] ≤ endIndices[i] ≤ n
Each character of s is either '*' or '|'

Sample Case 0

Input: "*|*|", [1],[3]
Sample Output
0 
Explanation:
The substring from index = 1 to index = 3 is '|'. There is no compartments in this string.

Sample Case 1
*|*|*|         s = "*|*|*|", [1],[6]
Sample Output
2 


The substring from index = 1 to index = 6 is '|*|*|'. There are two compartments in this string at (index = 2, index = 4) and (index = 4, index = 6). There are 2 items between these compartments.
'''

def get_numbers_of_items(s: str, startIndices, endIndices):
    separators = [] # --> a list of the indices of the separators
    for i, ch in enumerate(s):
        if ch == "|":
            separators.append(i)
    #separators = [0, 3, 5]
    num_items = [] #2
    for i in range(len(startIndices)):
        first_sep = get_first_separator(separators, startIndices[i] - 1) # 0, 0
        last_sep = get_last_separator(separators, endIndices[i]) # 3, 5
        if first_sep == -1 or last_sep == -1 or first_sep >= last_sep:
            num_items.append(0)
        else:
            first_sep_index, last_sep_index = separators.index(first_sep), separators.index(last_sep) #0, 2
            n = last_sep - first_sep - (last_sep_index - first_sep_index) 
            num_items.append(n)
    return num_items
            
    
def get_first_separator(separators, startIndex): #[0, 3, 5], 1
    for sep in separators:
        if sep >= startIndex:
            return sep #3
    return -1

def get_last_separator(separators, endIndex): #[0, 3, 5], 6
    for i in range(len(separators) - 1, -1, -1):
        sep = separators[i]
        if sep < endIndex:
            return sep #3
    return -1   


print(get_numbers_of_items("||||||", [1], [2])   
print(get_numbers_of_items("||||||", [1], [2])   
print(get_numbers_of_items("||||||", [1], [2])   

l = get_numbers_of_items(s, startIndices, endIndices)
print(l)