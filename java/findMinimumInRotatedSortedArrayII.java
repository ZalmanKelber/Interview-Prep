class Solution {
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1;
        //we will return the value of nums[l] when either l and r point to the same value or 
        //when l points to a smaller value than r
        while (l < r) {
            if (nums[l] < nums[r]) {
                return nums[l];
            }
            int med = l + (r - l) / 2;
            //if the mid pointer is greater than the left pointer, 
            //the solution can't be in between them.  If they're equal but not equal 
            //to the right pointer, then the solution also can't be in between them 
            if (nums[med] > nums[l] || (nums[med] == nums[l] && nums[l] != nums[r])) {
                l = med + 1;
            } else if (nums[med] < nums[l]) {
                r = med;
            } else {
                //if the values of all three are equal, we don't know where the solution is and must 
                //increment l one at a time
                l++;
            }
        }
        return nums[l];
    }
}