class Solution {
    public boolean checkValidString(String s) {
        if (s.length() == 0) { 
            return true; 
        }
        //keep track of star indices in a deque, so that we can add them and remove the first ones when necessary
        Deque<Integer> deque = new LinkedList<Integer>();
        //will keep track of the 'parentheses depth' (number of open parentheses subtracted by number of close parentheses) for each index of the string
        int[] parenDepths = new int[s.length()];
        int currentDepth = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '*') {
                deque.addLast(i);
            } else {
                currentDepth += c == '(' ? 1 : -1;
            }
            //if current depth is negative, convert the LEFTMOST remaining star into an open parenthesis.  If none exists, the string isn't valid: return False
            if (currentDepth < 0) {
                if (deque.size() == 0) { 
                    return false;
                }
                //update the paren_depths and current_depth to take into account the added open parenthesis
                int newOpenParenIndex = deque.removeFirst();
                for (int j = newOpenParenIndex; j < i; j++) {
                    parenDepths[j]++;
                }
                currentDepth++;
            }
            parenDepths[i] = currentDepth;  
        }
        //if the last parentheses depth isn't 0, we have a deficit of close parentheses.
        //find the RIGHTMOST remaining star and convert it into a close parenthesis, and check that this doesn't cause any new negative parentheses depths when updates
        while (parenDepths[s.length() - 1] != 0) {
            if (deque.size() == 0) {
                return false;
            }
            int newCloseParenIndex = deque.removeLast();
            for (int j = newCloseParenIndex; j < s.length(); j++) {
                if (parenDepths[j] == 0) {
                    return false;
                }
                parenDepths[j]--;
            }
        }
        return true;
    }
}