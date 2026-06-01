def remove_fourth_character(word: str) -> str:
    first_part = word[:3]
    last_part = word[4:]
    return first_part + last_part


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
