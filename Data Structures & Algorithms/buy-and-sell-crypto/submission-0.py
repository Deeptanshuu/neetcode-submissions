class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0

        i = 0
        profit = 0

        for i in range(len(prices) - 1):
            current = max(prices[i:]) - prices[i]
            if profit < current:
                profit = current
            i = i + 1

        return profit