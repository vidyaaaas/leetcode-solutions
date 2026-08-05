class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current_number = 0
        current_string = ""

        for character in s:
            if character.isdigit():
                current_number = current_number * 10 + int(character)
            elif character == "[":
                count_stack.append(current_number)
                string_stack.append(current_string)
                current_number = 0
                current_string = ""
            elif character == "]":
                repeat_count = count_stack.pop()
                previous_string = string_stack.pop()
                current_string = previous_string + current_string * repeat_count
            else:
                current_string += character

        return current_string
