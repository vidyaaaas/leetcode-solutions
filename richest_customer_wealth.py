from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum_wealth = 0

        for customer_accounts in accounts:
            maximum_wealth = max(maximum_wealth, sum(customer_accounts))

        return maximum_wealth
