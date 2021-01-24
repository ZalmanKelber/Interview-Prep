class Solution {
    //use merge sort with recursion
    public int[] sortArray(int[] nums) {
        //if we are in a base case, we can sumply return the array as is
        if (nums.length > 1) {
            //otherwise divide the array up into two sub probelms, solve them and then merge them together
            int[] leftSubProblem = sortArray(Arrays.copyOfRange(nums, 0, nums.length / 2));
            int[] rightSubProblem = sortArray(Arrays.copyOfRange(nums, nums.length / 2, nums.length));
            int ptr1 = 0;
            int ptr2 = 0;
            for (int i = 0; i < nums.length; i++) {
                if (ptr1 == leftSubProblem.length || (ptr2 < rightSubProblem.length && 
                                                     rightSubProblem[ptr2] < leftSubProblem[ptr1])) {
                    nums[i] = rightSubProblem[ptr2];
                    ptr2++;
                } else {
                    nums[i] = leftSubProblem[ptr1];
                    ptr1++;
                }
            }
        }
        return nums;
    }
}