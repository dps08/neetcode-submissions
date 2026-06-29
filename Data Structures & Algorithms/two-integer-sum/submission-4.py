class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        hashmap = {}
        for index, value in enumerate(nums):
            if (target - value) in hashmap:
                return [hashmap[target - value], index]
            hashmap[value] = index