from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for index, number in enumerate(nums):
            if number in last_seen and index - last_seen[number] <= k:
                return True

            last_seen[number] = index

        return False
