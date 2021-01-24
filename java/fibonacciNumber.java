class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();
    
    public int fib(int n) {
        //recursive base cases
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        //check if we've already solved this problem
        if (memo.keySet().contains(n)) {
            return memo.get(n);
        }
        //get result recursively and add it to memo
        int result = fib(n - 1) + fib(n - 2);
        memo.put(n, result);
        return result;
    }
}