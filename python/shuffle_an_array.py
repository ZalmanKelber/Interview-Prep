class Solution:

    def __init__(self, nums: List[int]):
        self._list = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self._list

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        copy = self._list[:]
        random.shuffle(copy)
        return copy