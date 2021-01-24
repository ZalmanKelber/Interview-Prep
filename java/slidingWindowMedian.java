class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] medians = new double[nums.length + 1 - k];
        //store the sorted subarray in sortedWindow
        int[] sortedWindow = Arrays.copyOfRange(nums, 0, k);
        Arrays.sort(sortedWindow);
        for (int i = k; i <= nums.length; i++) {
            //find the median of the sorted subarray, then slide it over
            if (k % 2 == 0) {
                medians[i - k] = (double) sortedWindow[k / 2] / 2 + (double) sortedWindow[(k / 2) - 1] / 2;
            } else {
                medians[i - k] = sortedWindow[(k - 1) / 2];
            }
            if (i < nums.length) {
                removeAndInsert(sortedWindow, nums[i - k], nums[i]);
            }
        }
        return medians;
    }
    
    private void removeAndInsert(int[] sortedWindow, int toRemove, int toInsert) {
        //find index of element to be removed
        int removeIndex = 0;
        while (sortedWindow[removeIndex] != toRemove) {
            removeIndex++;
        }
        //remove it by moving all subsequent elements one index to the left
        for (int i = removeIndex; i < sortedWindow.length - 1; i++) {
            sortedWindow[i] = sortedWindow[i + 1];
        }
        //find the index to insert the next element
        int insertIndex = 0;
        while (insertIndex < sortedWindow.length - 1 && sortedWindow[insertIndex] < toInsert) {
            insertIndex++;
        }
        //move over every subsequent element one index to the left and then insert it
        for (int i = sortedWindow.length - 1; i > insertIndex; i--) {
            sortedWindow[i] = sortedWindow[i - 1];
        }
        sortedWindow[insertIndex] = toInsert;
    }
}