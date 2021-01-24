class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        #keep track of which numbers are still eligible: that is, the numbers that have appeared at least once on every domino thus far
        eligible = { A[0], B[0] }
        #for each eligible number, keep track of the number of indices it appear in the upper and lower levels
        class Solution:
        upper_and_lower_indices = dict()
        for num in eligible:
            upper_and_lower_indices[num] = { "upper": 0, "lower": 0 }
        #iterate through each domino
        for i in range(len(A)):
            to_remove = set()
            #if a number doesn't appear in the domino, it is no longer eligible
            for el in eligible:
                if el not in { A[i], B[i] }:
                    to_remove.add(el)
            for el in to_remove:
                eligible.remove(el)
            #if there are no eligible numbers, there is no solution
            if len(eligible) == 0:
                return -1
            #update indices count for remaining elibile numbers
            if A[i] in eligible:
                upper_and_lower_indices[A[i]]["upper"] += 1
            if B[i] in eligible:
                upper_and_lower_indices[B[i]]["lower"] += 1
        #determine the minimum number of rotations by finding the eligible number with the greatest number of indices in either position
        min_rotations = len(A)
        for el in eligible:
            for position in ["upper", "lower"]:
                min_rotations = min(min_rotations, len(A) - upper_and_lower_indices[el][position])
        return min_rotations