class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        square_root = 0

        while left <= right:
            middle = left + (right - left) // 2
            square = middle * middle

            if square <= x:
                square_root = middle
                left = middle + 1
            else:
                right = middle - 1

        return square_root
