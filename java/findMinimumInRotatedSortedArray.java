class Solution {
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1;
        //in the final result, l will point to the minimum and r will be greater or equal to l
        while (nums[l] > nums[r]) {
            int med = l + (r - l) / 2;
            if (nums[med] >= nums[l]) {
                l = med + 1;
            } else {
                r = med;
            }
        }
        return nums[l];
    }
}