import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap_order = []
    reverse_sort = []
    for num in nums:
        heapq.heappush(heap_order, -num)
    
    while heap_order:
        reverse_sort.append(-heapq.heappop(heap_order))

    return reverse_sort




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
