 class Solution {
    public String removeOuterParentheses(String S) {
        //traverse the string and keep track of the paren_depth – the number of open parens subtracted by the number of close parens
        int parenDepth = 0;
        //store the characters that aren't removed in a list to allow for constant time insertion
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            //use paren_depth to determine whether or not a character is an outer-layer parenthesis
            if ((parenDepth != 0 || c != '(') && (parenDepth != 1 || c != ')')) {
                sb.append(c);
            }
            parenDepth += c == '(' ? 1 : -1;
        }
        return sb.toString();
    }
}

//problem: https://leetcode.com/problems/remove-outermost-parentheses