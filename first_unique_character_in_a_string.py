class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}

        for character in s:
            frequency[character] = frequency.get(character, 0) + 1

        for index, character in enumerate(s):
            if frequency[character] == 1:
                return index

        return -1
