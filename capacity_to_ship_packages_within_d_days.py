from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            capacity = left + (right - left) // 2
            days_needed = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = 0
                current_load += weight

            if days_needed <= days:
                right = capacity
            else:
                left = capacity + 1

        return left
