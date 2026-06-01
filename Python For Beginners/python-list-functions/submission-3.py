from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

def get_min(nums: List[int]) -> int:
    low = nums[0]
    for i in range(len(nums)):
        if low>=nums[i]:
            low = nums[i]
    return low

def get_max(nums: List[int]) -> int:
    high = nums[0]
    for i in range(len(nums)):
        if high<=nums[i]:
            high = nums[i]
    return high

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
