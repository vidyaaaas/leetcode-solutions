class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        if window_size > len(s2):
            return False

        required_counts = [0] * 26
        window_counts = [0] * 26

        for index in range(window_size):
            required_counts[ord(s1[index]) - ord("a")] += 1
            window_counts[ord(s2[index]) - ord("a")] += 1

        if window_counts == required_counts:
            return True

        for right in range(window_size, len(s2)):
            window_counts[ord(s2[right]) - ord("a")] += 1
            window_counts[ord(s2[right - window_size]) - ord("a")] -= 1

            if window_counts == required_counts:
                return True

        return False
