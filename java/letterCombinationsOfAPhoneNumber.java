class Solution {

    Map<Character, Character[]> numbersToLetters = new HashMap();
    //store stck as a StringBuilder to allow constant time insertion and removal
    StringBuilder stack = new StringBuilder();
    String digits = "";
    List<String> solutions = new ArrayList();
    
    public List<String> letterCombinations(String digits) {
        this.digits = digits;
        initializeMap();
        backtrack();
        return solutions;
    }
    
    private void backtrack() {
        //if the stack is currently full, add it to the list of solutions
        if (stack.length() == digits.length()) {
            if (stack.length() > 0) {
                solutions.add(stack.toString());
            }
            return;
        }
        //otherwise, call the backtrack function for each possible next character
        for (char c : numbersToLetters.get(digits.charAt(stack.length()))) {
            stack.append(c);
            backtrack();
            stack.deleteCharAt(stack.length() - 1);
        }
    }
    
    private void initializeMap() {
        numbersToLetters.put('2', new Character[]{ 'a', 'b', 'c' });
        numbersToLetters.put('3', new Character[]{ 'd', 'e', 'f' });
        numbersToLetters.put('4', new Character[]{ 'g', 'h', 'i' });
        numbersToLetters.put('5', new Character[]{ 'j', 'k', 'l' });
        numbersToLetters.put('6', new Character[]{ 'm', 'n', 'o' });
        numbersToLetters.put('7', new Character[]{ 'p', 'q', 'r', 's' });
        numbersToLetters.put('8', new Character[]{ 't', 'u', 'v' });
        numbersToLetters.put('9', new Character[]{ 'w', 'x', 'y', 'z' });
    }
}