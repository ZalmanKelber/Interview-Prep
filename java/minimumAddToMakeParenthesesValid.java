class Solution {
    public int minAddToMakeValid(String S) {
        int numNeeded = 0; //number of parentheses needed to insert to make string valid; updates at the end of every 'segment'
        int openParens = 0; //number of open parentheses in the current 'segment'
        int closeParens = 0;
        //traverse the string and end a 'segment' when the number of close parentheses is greater than the number of open parentheses
        //increment numNeeded at the end of each such segment by one, which corresponds to the open parenthesis needed to make the segment valid
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            if (c == '(') {
                openParens++;
            } else {
                closeParens++;
            }
            if (closeParens > openParens) {
                numNeeded++;
                openParens = 0;
                closeParens = 0;
            }
        }
        //add to numNeeded the number of close parentheses necessary to close out the remaining excess open parentheses
        numNeeded += openParens - closeParens;
        return numNeeded;
    }
}