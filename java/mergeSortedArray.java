class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        //pointer1 will traverse nums1 in reverse
        int pointer1 = m - 1;
        //pointer2 will traverse nums2 in reverse
        int pointer2 = n - 1;
        //i traverses the full nums1 in reverse
        for (int i = m + n - 1; i >= 0; i--) {
            if (pointer1 < 0 || (pointer2 >= 0 && nums2[pointer2] > nums1[pointer1])) {
                nums1[i] = nums2[pointer2];
                pointer2--;
            } else {
                nums1[i] = nums1[pointer1];
                pointer1--;
            }
        }
    }
}