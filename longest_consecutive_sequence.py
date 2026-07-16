from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for num in numbers:
            # Only start counting when this is the first number of a sequence.
            if num - 1 not in numbers:
                current = num
                length = 1

                while current + 1 in numbers:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
