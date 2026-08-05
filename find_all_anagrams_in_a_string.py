from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_size = len(p)

        if window_size > len(s):
            return []

        required_counts = [0] * 26
        window_counts = [0] * 26
        answer = []

        for index in range(window_size):
            required_counts[ord(p[index]) - ord("a")] += 1
            window_counts[ord(s[index]) - ord("a")] += 1

        if window_counts == required_counts:
            answer.append(0)

        for right in range(window_size, len(s)):
            window_counts[ord(s[right]) - ord("a")] += 1
            window_counts[ord(s[right - window_size]) - ord("a")] -= 1

            if window_counts == required_counts:
                answer.append(right - window_size + 1)

        return answer
