from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # buckets[count] stores all numbers that appear "count" times.
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in frequency.items():
            buckets[count].append(num)

        answer = []

        # Read from the highest frequency down to the lowest.
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                answer.append(num)

                if len(answer) == k:
                    return answer

        return answer
