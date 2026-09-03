from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temporary = [0] * len(nums)

        def merge_sort(left: int, right: int) -> None:
            if right - left <= 1:
                return

            middle = (left + right) // 2
            merge_sort(left, middle)
            merge_sort(middle, right)

            first = left
            second = middle
            write = left

            while first < middle and second < right:
                if nums[first] <= nums[second]:
                    temporary[write] = nums[first]
                    first += 1
                else:
                    temporary[write] = nums[second]
                    second += 1
                write += 1

            while first < middle:
                temporary[write] = nums[first]
                first += 1
                write += 1

            while second < right:
                temporary[write] = nums[second]
                second += 1
                write += 1

            nums[left:right] = temporary[left:right]

        merge_sort(0, len(nums))
        return nums
