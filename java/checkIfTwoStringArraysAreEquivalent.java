class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        //the pointers will traverse the words at the same time
        int[] ptr1 = new int[]{ 0, 0 };
        int[] ptr2 = new int[]{ 0, 0 };
        //once one of the pointers reached the end, we can exit the loop
        while (ptr1[0] < word1.length && ptr2[0] < word2.length) {
            //determine if the characters are a match
            char c1 = word1[ptr1[0]].charAt(ptr1[1]);
            char c2 = word2[ptr2[0]].charAt(ptr2[1]);
            if (c1 != c2) {
                return false;
            }
            //increment each pointer
            if (ptr1[1] == word1[ptr1[0]].length() - 1) {
                ptr1[0]++;
                ptr1[1] = 0;
            } else {
                ptr1[1]++;
            }
            if (ptr2[1] == word2[ptr2[0]].length() - 1) {
                ptr2[0]++;
                ptr2[1] = 0;
            } else {
                ptr2[1]++;
            }
        }
        //if the other pointer hasn't completed, the arrays aren't a match
        if (ptr2[0] != word2.length || ptr1[0] != word1.length) {
            return false;
        }
        return true;
    }
}