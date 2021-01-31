class Solution {
    int curIndex = 0;
    String s = "";
    List<String> wordDict = new ArrayList();
    Map<Integer, Boolean> memo = new HashMap();
    
    public boolean wordBreak(String s, List<String> wordDict) {
        this.s = s;
        this.wordDict = wordDict;
        memo.put(s.length(), true);
        return backtrack();
    }
    
    private boolean backtrack() {
        if (!memo.keySet().contains(curIndex)) {
            for (String word : wordDict) {
                if (word.length() <= s.length() - curIndex) {
                    if (s.substring(curIndex, curIndex + word.length()).equals(word)) {
                        curIndex += word.length();
                        if (backtrack()) {
                            return true;
                        }
                        curIndex -= word.length();
                    }
                    
                }
            }
            memo.put(curIndex, false);
        }
        return memo.get(curIndex);
    }
}