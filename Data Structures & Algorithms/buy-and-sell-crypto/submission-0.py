class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        max_profit=0
        min_price=float('inf')
        for price in prices:
            profit=0
            min_price=min(min_price,price)
            profit=price-min_price
            max_profit=max(max_profit,profit)
        return max_profit