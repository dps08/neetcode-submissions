class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_prev = 0
        count_new = 0
        for num in nums:
            if num ==1:
                count_new += 1
                count_prev = max(count_prev, count_new)
            else:  
                count_new = 0
        return count_prev

