class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if stack and matching[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []