class Solution {
    public int longestValidParentheses(String s) {
        //check in both directions and take the max
        String reverse_s = reverseParentheses(s);
        return Math.max(longestForward(s), longestForward(reverse_s));
    }
    
    public int longestForward(String s) {
        //we'll be searching for substrings where the depth at the startIndex is one greater than the depth at the end
        int curDepth = 0;
        //set startIndex to -1 and startDepth to 0 when we're not currently searching a substring
        int startIndex = -1;
        int startDepth = 0;
        int longest_found = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            boolean isOpen = c == '(';
            curDepth += isOpen ? 1 : -1;
            if (isOpen && startIndex == -1) {
                startIndex = i;
                startDepth = curDepth;
            }
            //if the present index forms a valid substring with the present startIndex, 
            //see if this substring is the longest we've found so far
            if (!isOpen && startIndex != -1 && startDepth - 1 == curDepth) {
                longest_found = Math.max(longest_found, i + 1 - startIndex);
                //if there are no more valid substrings with this startIndex, start a new segment by
                //resetting startIndex and startDepth
                if (i == s.length() - 1 || s.charAt(i + 1) == ')') {
                    startIndex = -1;
                    startDepth = 0;
                }
            }
        }
        return longest_found;
    }
    
    public String reverseParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i) == ')' ? '(' : ')';
            sb.append(c);
        }
        return sb.toString();
    }
}