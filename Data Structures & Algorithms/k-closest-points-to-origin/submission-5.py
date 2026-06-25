import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for pt in points:
            d = pt[0]**2 + pt[1]**2
            heapq.heappush(heap, (-d, pt))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for h in heap:
            result.append(h[1])
        
        return result