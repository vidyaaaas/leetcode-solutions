from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            speed = left + (right - left) // 2
            hours_needed = sum(
                (pile + speed - 1) // speed for pile in piles
            )

            if hours_needed <= h:
                right = speed
            else:
                left = speed + 1

        return left
