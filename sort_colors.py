from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sort 0s, 1s, and 2s in-place using the Dutch National Flag algorithm."""
        low = 0
        current = 0
        high = len(nums) - 1

        while current <= high:
            if nums[current] == 0:
                nums[low], nums[current] = nums[current], nums[low]
                low += 1
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1
