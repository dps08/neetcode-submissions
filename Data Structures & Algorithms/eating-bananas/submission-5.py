import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(piles, k):
            total = 0
            for pile in piles:
                total += math.ceil(pile/k)
            return total

        
        low = 1
        high = max(piles)
        while low != high:
            mid = (low + high) // 2
            if hours_needed(piles, mid) <= h:
                high = mid
            else:
                low = mid + 1
        
        return low
