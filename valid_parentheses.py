class Solution:
    def isValid(self, s: str) -> bool:
        matching_opening = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for bracket in s:
            if bracket in matching_opening:
                if not stack or stack.pop() != matching_opening[bracket]:
                    return False
            else:
                stack.append(bracket)

        return not stack
