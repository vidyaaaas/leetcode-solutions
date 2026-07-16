from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # A set removes duplicates, because the answer needs unique values.
        numbers_in_first = set(nums1)
        answer = set()

        for num in nums2:
            if num in numbers_in_first:
                answer.add(num)

        return list(answer)
