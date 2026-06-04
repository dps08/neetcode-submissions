from typing import List

def read_integers() -> List[int]:
    numbers_with_comma = input()
    numbers_in_list = numbers_with_comma.split(",")
    return[int(x) for x in numbers_in_list ]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
