class Solution {
    public int numRescueBoats(int[] people, int limit) {
        //keep track of the number of people per weight
        int[] peoplePerWeight = new int[limit + 1];
        for (int person : people) {
            peoplePerWeight[person]++;
        }
        //light and heavy pointers will traverse peoplePerWeight in opositte directions looking for matches
        int lightPointer = 0;
        int heavyPointer = limit;
        int numTwoPersonBoats = 0;
        while (heavyPointer > lightPointer && numTwoPersonBoats * 2 < people.length) {
            //lightPointer will always point to the weight of the lightest remaining person
            while (peoplePerWeight[lightPointer] == 0) {
                lightPointer++;
            }
            //heavyPointer will always point to the weight of the heaviest valid match
            while (heavyPointer > lightPointer && 
                   (peoplePerWeight[heavyPointer] == 0 || heavyPointer + lightPointer > limit )) {
                heavyPointer--;
            }
            if (heavyPointer > lightPointer) {
                numTwoPersonBoats++;
                peoplePerWeight[lightPointer]--;
                peoplePerWeight[heavyPointer]--;
            }
        }
        //if the light and heavy pointers are pointing to the same weight, pair off the remaining people at that weight
        if (lightPointer * 2 <= limit) {
            numTwoPersonBoats += peoplePerWeight[lightPointer] / 2;
        }
        return people.length - numTwoPersonBoats;
    }
}