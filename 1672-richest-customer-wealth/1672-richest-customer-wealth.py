class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for account in accounts:
            account_sum = sum(account)
            richest = max(account_sum, richest)
        return richest
        