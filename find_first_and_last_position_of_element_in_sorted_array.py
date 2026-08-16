from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_position = self._find_boundary(nums, target, find_first=True)

        if first_position == -1:
            return [-1, -1]

        last_position = self._find_boundary(nums, target, find_first=False)
        return [first_position, last_position]

    def _find_boundary(
        self, nums: List[int], target: int, find_first: bool
    ) -> int:
        left = 0
        right = len(nums) - 1
        position = -1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                position = middle
                if find_first:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return position
