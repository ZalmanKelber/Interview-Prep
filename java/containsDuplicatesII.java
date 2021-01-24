class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        //store the last k values in a hash set for constant time lookup
        Set<Integer> lastKValues = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            //if the next value is contained in the last k values, return true
            if (lastKValues.contains(nums[i])) {
                return true;
            }
            //add the next value and, if necessary, remove the first element
            lastKValues.add(nums[i]);
            if (i >= k) {
                lastKValues.remove(nums[i - k]);
            }
        }
        return false;
    }
}