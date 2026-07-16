from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]

        for number in nums:
            new_sum = self.prefix_sum[-1] + number
            self.prefix_sum.append(new_sum)

    def sumRange(self, left: int, right: int) -> int:
        sum_before_left = self.prefix_sum[left]
        sum_through_right = self.prefix_sum[right + 1]

        return sum_through_right - sum_before_left
