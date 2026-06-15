class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_prev = 0
        count_new = 0
        for i in range(len(nums)):
            if nums[i] ==1:
                count_new += 1
            else:
                count_prev = max(count_prev, count_new)
                count_new = 0
        count_prev = max(count_prev, count_new)
        return count_prev

