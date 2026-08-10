class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        left = 0
        highest_frequency = 0
        longest_length = 0

        for right, character in enumerate(s):
            frequencies[character] = frequencies.get(character, 0) + 1
            highest_frequency = max(highest_frequency, frequencies[character])

            window_length = right - left + 1
            if window_length - highest_frequency > k:
                frequencies[s[left]] -= 1
                left += 1

            longest_length = max(longest_length, right - left + 1)

        return longest_length
