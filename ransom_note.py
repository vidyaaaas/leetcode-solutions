class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available_characters = {}

        for character in magazine:
            available_characters[character] = (
                available_characters.get(character, 0) + 1
            )

        for character in ransomNote:
            if available_characters.get(character, 0) == 0:
                return False

            available_characters[character] -= 1

        return True
