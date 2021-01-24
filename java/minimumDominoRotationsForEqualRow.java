class Solution {
    public int minDominoRotations(int[] A, int[] B) {
        //keep track of the eligible numbers (that is, the numbers that appear in every such domino)
        Set<Integer> eligible = new HashSet<>();
        eligible.add(A[0]);
        eligible.add(B[0]);
        //for each eligible number, keep track of the number of times it appears in the upper and lower positions
        Map<Integer, Integer[]> indexCount = new HashMap<>();
        for (int el : eligible) {
            indexCount.put(el, new Integer[]{ 0, 0 });
        }
        //iterate through the dominos
        for (int i = 0; i < A.length; i++) {
            //remove from the eligible set any numbers that don't appear
            Set<Integer> toRemove = new HashSet<>();
            for (int el : eligible) {
                if (el != A[i] && el != B[i]) {
                    toRemove.add(el);
                }
            }
            for (int el : toRemove) {
                eligible.remove(el);
            }
            //if there are no more eligible numbers, there is no solution
            if (eligible.size() == 0) {
                return -1;
            }
            //increment upper and lower indices for each eligible number
            if (eligible.contains(A[i])) {
                Integer[] curIndexCount = indexCount.get(A[i]);
                curIndexCount[1]++;
            }
            if (eligible.contains(B[i])) {
                Integer[] curIndexCount = indexCount.get(B[i]);
                curIndexCount[0]++;
            }
        }
        //find the greatest number of indicies among eligible numbers and positions, and substract it 
        //from the number of dominos to get the minimum number of rotations
        int minRotations = A.length;
        for (int el : eligible) {
            for (int i = 0; i < 2; i++) {
                minRotations = Math.min(minRotations, A.length - indexCount.get(el)[i]);
            }
        }
        return minRotations;
    }
}