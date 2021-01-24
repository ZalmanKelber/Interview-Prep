class Solution {
    public int findKthLargest(int[] nums, int k) {
        //keep k elements in a heap
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int i = 0; i < nums.length; i++) {
            //traverse the array and add and remove elements from the heap so that the k largest elements stay in heap
            queue.add(nums[i]);
            if (i >= k) {
                queue.poll();
            }
        }
        //the smallest of the k largest elements is the result we want
        return queue.poll();
    }
}