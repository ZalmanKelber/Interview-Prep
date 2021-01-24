class Solution {
    public double findMaxAverage(int[] nums, int k) {
        //get average of first k elements
        double currentAverage = 0;
        for (int i = 0; i < k; i++) {
            currentAverage += nums[i];
        }
        currentAverage /= k;
        //keep track of maximum average
        double maxAverage = currentAverage;
        for (int i = k; i < nums.length; i++) {
            //obtain the next current average by adding next element and removing first element
            currentAverage -= ((double) nums[i - k]) / k;
            currentAverage += ((double) nums[i]) / k;
            maxAverage = Math.max(maxAverage, currentAverage);
        }
        return maxAverage;
    }
}