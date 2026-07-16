class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_count = {}

        for letter in s:
            letter_count[letter] = letter_count.get(letter, 0) + 1

        for letter in t:
            if letter not in letter_count:
                return False

            letter_count[letter] -= 1

            if letter_count[letter] < 0:
                return False

        return True
