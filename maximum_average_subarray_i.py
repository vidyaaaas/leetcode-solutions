from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        maximum_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[right - k]
            maximum_sum = max(maximum_sum, window_sum)

        return maximum_sum / k
