class Solution {
    public int removeDuplicates(int[] nums) {
        //penum and antiPenum store previous values in order to determine whether the present value in the traversal is a duplicate
        int penum = nums[0] - 1;
        int antiPenum = nums[0] - 1;
        //readPointer traverses the array reading each element and determining if it's a duplicate and whether it should be retained
        int readPointer = 0;
        //writePointer points to the indices where the retained elements should appear in the final array
        int writePointer = 0;
        while (readPointer < nums.length) {
            //if the read value isn't a duplicate, insert it into the array at the correct spot
            if (nums[readPointer] != antiPenum) {
                nums[writePointer] = nums[readPointer];
                writePointer++;
            }
            //update the other values
            antiPenum = penum;
            penum = nums[readPointer];
            readPointer++;
        }
        return writePointer;
    }
}