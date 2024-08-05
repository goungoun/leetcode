# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Maximize profit with the best decision when to buy and sell
        return max_profit

        Approach:
        Let's assume that I bought stock the day 1 and Iterate the prices to simulate the profit. 
        If the price is lower than before, wrong decision in the past. That is the time to buy.
        If the price is higher than before, time to sell. Update the maximum profit.

        Example 1:
        prices = [7,1,5,3,6,4]

        Example 2:
        prices = [7,6,4,3,1]
        """

        max_profit = 0
        profit = 0

        buy = prices[0]
        for price in prices:
            if buy > price: 
                buy = price
            else:
                max_profit = max(max_profit, price - buy) 

        return max_profit
