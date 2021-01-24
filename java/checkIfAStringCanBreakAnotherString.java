class Solution {
    public boolean checkIfCanBreak(String s1, String s2) {
        int l = s1.length();
        //store each string as an array of numbers, corresponding to the ascii values
        int[] nums1 = new int[l];
        int[] nums2 = new int[l];
        for (int i = 0; i < l; i++) {
            nums1[i] = (int) s1.charAt(i);
            nums2[i] = (int) s2.charAt(i);
        }
        //sort the arrays
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        boolean s1BreaksS2 = true;
        boolean s2BreaksS1 = true;
        //compare the arrays one number at a time to determine if one breaks the other 
        for (int i = 0; i < l; i++) {
            if (nums1[i] > nums2[i]) {
                s2BreaksS1 = false;
            }
            if (nums2[i] > nums1[i]) {
                s1BreaksS2 = false;
            }
            if (!s1BreaksS2 && !s2BreaksS1) {
                return false;
            }
        }
        return true;
    }
}