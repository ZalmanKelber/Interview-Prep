class Solution {
    public int search(int[] nums, int target) {
        //initialize pointers to opossite sides of array
        int l = 0, r = nums.length - 1;
        //modify pointers until there are no values in between
        while (l + 1 < r) {
            int med = l + (r - l) / 2;
            if (nums[med] == target) { return med; }
            if (nums[med] > target) { r = med - 1; }
            else { l = med + 1; }
        }
        //check if final values of pointers point to target
        if (l < nums.length && nums[l] == target) { return l; }
        if (r >= 0 && nums[r] == target) { return r; }
        return -1;
    }
}