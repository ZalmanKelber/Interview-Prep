class Solution {
    
    //store stack and solutions outside of recursion flow
    Stack<Integer> stack = new Stack();
    int[] nums = new int[0];
    List<List<Integer>> solutions = new ArrayList();
    
    public List<List<Integer>> subsets(int[] nums) {
        this.nums = nums;
        backtrack(0);
        return solutions;
    }
    
    private void backtrack(int index) {
        //if we've gone through the list of nums, add the present stack to the list of solutions
        if (index == nums.length) {
            solutions.add(new ArrayList(stack));
            return;
        }
        //call the next backtrack function both with nums[index] and without nums[index]
        backtrack(index + 1);
        stack.add(nums[index]);
        backtrack(index + 1);
        stack.pop();
    }
}