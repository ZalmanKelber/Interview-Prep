class Solution {
    public int scoreOfParentheses(String S) {
        //recursion base case
        if (S.length() <= 4) {
            return S.length() / 2;
        }
        //depth is the number of open parentheses minus the number of close parentheses
        int parenDepth = 0;
        //'segments' are the outer-layer substrings of parentheses (i.e. ones not enclosed within any other outler layer)
        List<Integer> segmentEndpoints = new ArrayList<Integer>();
        segmentEndpoints.add(0);
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            parenDepth += c == '(' ? 1 : -1;
            //if depth is zero, we've reached the end of a 'segment'
            if (parenDepth == 0) {
                segmentEndpoints.add(i + 1);
            }
        }
        int score = 0;
        //add up the subscores of each segment
        for (int i = 0; i < segmentEndpoints.size() - 1; i++) {
            int startIndex = segmentEndpoints.get(i) + 1;
            int endIndex = segmentEndpoints.get(i + 1) - 1;
            if (startIndex == endIndex) {
                score++;
            } else {
                score += 2 * scoreOfParentheses(S.substring(startIndex, endIndex));
            }
        }
        return score;
    }
}