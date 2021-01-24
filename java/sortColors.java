class Solution {
    public void sortColors(int[] nums) {
        //keep track of the number of each of the three colors in an array
        int[] colorCount = new int[3];
        //traverse the array and read each new element
        for (int i = 0; i < nums.length; i++) {
            int next_color = nums[i];
            switch (next_num) {
                //if the color is 1, add a 1 after the last existing 1
                //if there is at least one 2, move the deleted 2 up to the current index
                case 1:
                    nums[colorCount[0] + colorCount[1]] = 1;
                    if (colorCount[2] > 0) {
                        nums[i] = 2;
                    }
                    break;
                //if the color is 0, add it to the beginning and bubble up any displaced colors
                case 0:
                    nums[colorCount[0]] = 0;
                    if (colorCount[1] > 0) {
                        nums[colorCount[0] + colorCount[1]] = 1;
                    }
                    if (colorCount[2] > 0) {
                        nums[i] = 2;
                    }
                default:
                    break;      
            }
            //update the new color count
            colorCount[next_color]++;
        }
    }
}