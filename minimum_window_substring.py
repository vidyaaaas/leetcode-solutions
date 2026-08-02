class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        required_counts = {}

        for character in t:
            required_counts[character] = required_counts.get(character, 0) + 1

        window_counts = {}
        required = len(required_counts)
        formed = 0
        left = 0
        best_start = 0
        best_length = float("inf")

        for right, character in enumerate(s):
            window_counts[character] = window_counts.get(character, 0) + 1

            if (
                character in required_counts
                and window_counts[character] == required_counts[character]
            ):
                formed += 1

            while formed == required:
                window_length = right - left + 1

                if window_length < best_length:
                    best_start = left
                    best_length = window_length

                left_character = s[left]
                window_counts[left_character] -= 1

                if (
                    left_character in required_counts
                    and window_counts[left_character]
                    < required_counts[left_character]
                ):
                    formed -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start : best_start + best_length]
