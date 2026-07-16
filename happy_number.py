class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            # Seeing the same number again means we are stuck in a loop.
            if n in seen:
                return False

            seen.add(n)
            next_number = 0

            while n > 0:
                digit = n % 10
                next_number += digit * digit
                n //= 10

            n = next_number

        return True
