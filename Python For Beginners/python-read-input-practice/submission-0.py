def add_two_numbers() -> int:
    nums_input = input()
    nums = nums_input.split(",")
    sum = 0
    for i in nums:
        sum += int(i)
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
