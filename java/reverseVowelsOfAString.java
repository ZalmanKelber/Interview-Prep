
//slow solution:

// class Solution {
//     public String reverseVowels(String s) {
//         Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
//         List<Character> vowelStack = new ArrayList<>();
//         List<Integer> vowelIndices = new ArrayList<>();
//         char[] result = new char[s.length()];
//         for (int i = 0; i < s.length(); i++) {
//             char c = s.charAt(i);
//             if (vowels.contains(Character.toLowerCase(c))) {
//                 vowelStack.add(c);
//                 vowelIndices.add(i);
//             } else {
//                 result[i] = c;
//             }
//         }
//         for (int i = 0; i < vowelIndices.size(); i++) {
//             int resultIndex = vowelIndices.get(i);
//             char nextChar = vowelStack.get(vowelStack.size() - 1 - i);
//             result[resultIndex] = nextChar;
//         }
//         return new String(result);
//     }
// }


class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        //string builder will allow us to change characters of the string in place
        StringBuilder sb = new StringBuilder(s);
        int leftPointer = -1;
        int rightPointer = s.length();
        //the left and right pointers will traverse the string and fine one vowel at a time and switch them
        while (rightPointer > leftPointer) {
            do {
                leftPointer++;
            }
            while (leftPointer < s.length() && !vowels.contains(Character.toLowerCase(sb.charAt(leftPointer))));
            do {
                rightPointer--;
            }
            while (rightPointer >= 0 && !vowels.contains(Character.toLowerCase(sb.charAt(rightPointer))));
            if (rightPointer > leftPointer) {
                char c = sb.charAt(leftPointer);
                sb.setCharAt(leftPointer, sb.charAt(rightPointer));
                sb.setCharAt(rightPointer, c);
            }  
        }
        return sb.toString();
    }
}