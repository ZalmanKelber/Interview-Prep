class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        found_quadruplets = set()
        sums_by_duplet = defaultdict(list)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                duplet_sum = nums[i] + nums[j]
                if target - duplet_sum in sums_by_duplet:
                    for (k, l) in sums_by_duplet[target - duplet_sum]:
                        if k not in [i, j] and l not in [i, j]:
                            found_quadruplets.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
                sums_by_duplet[duplet_sum].append((i, j))
        return [list(quad) for quad in found_quadruplets]
                