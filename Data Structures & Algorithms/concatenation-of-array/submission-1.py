class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):       # runs 2 times
            for num in nums:     # runs n times
                ans.append(num)
        return ans
        