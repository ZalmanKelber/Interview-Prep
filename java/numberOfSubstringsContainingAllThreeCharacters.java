class Solution {
    public int numberOfSubstrings(String s) {
        int totalSubstrings = 0;
        //map will keep track of how many of each character is currently in each substring
        Map<Character, Integer> numChars = new HashMap<>();
        numChars.put('a', 0);
        numChars.put('b', 0);
        numChars.put('c', 0);
        int substringEnd = -1;
        int substringStart = 0;
        while (substringEnd < s.length()) {
            //increment substringEnd until the substring contains all three characters
            while (!containsAbc(numChars) && substringEnd < s.length()) {
                substringEnd++;
                if (substringEnd < s.length()) {
                    numChars.put(s.charAt(substringEnd), numChars.get(s.charAt(substringEnd)) + 1);
                }
            }
            //if there are no possible substrings, break from the loop
            if (substringEnd >= s.length()) {
                break;
            }
            //increment the total by all substrings with the given starting index and an ending index equal to or greater than the current end index
            totalSubstrings += s.length() - substringEnd;
            //increment the starting index and remove the first character of the substring from the set
            numChars.put(s.charAt(substringStart), numChars.get(s.charAt(substringStart)) - 1);
            substringStart++;
        }
        return totalSubstrings;
    }
        
    public boolean containsAbc(Map numChars) {
        if ((int) numChars.get('a') == 0 || (int) numChars.get('b') == 0 || (int) numChars.get('c') == 0) {
            return false;
        }
        return true;
    }
}